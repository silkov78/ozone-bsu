# ozone-bsu

Сайт ННИЦ МО БГУ (Национальный научно-исследовательский центр мониторинга озоносферы).
Стек: Django 4.2 + PostgreSQL 16 + Nginx, всё в Docker Compose.

Подробнее: [docs/](docs/README.md) — статус работ, архитектура и структура сайта.

## Структура репозитория

```
app/                  Django-проект (config, main_app, observations, staff, templates, static, locale)
docker/
  django/             Dockerfile (прод), Dockerfile.dev, entrypoint.sh, certs/ (корп. CA, необязательно)
  nginx/              nginx.conf, ozone.conf (прод, HTTPS), ozone.dev.conf
  initdb/             автозаливка дампа в dev-БД
scripts/              backup.sh, restore_db.sh, deploy.sh, manage.sh
compose.yml           продакшен (код собирается в образ, gunicorn)
compose.dev.yml       разработка (./app монтируется, runserver)
.env.dev              переменные dev (в git)
.env.example          шаблон переменных прода → скопировать в .env (не в git)
local_data/           дамп БД, медиа и выгрузки для dev (не в git)
```

Во всех сервисах: `restart: always` и healthcheck-и. Django отдаёт `/healthz/` (приложение + БД),
Nginx — `/nginx-health`. Запуск идёт по цепочке postgres (healthy) → django (healthy) → nginx.

## Разработка

1. Положить в `local_data/`: `backup_*.sql` (дамп БД) и `media/` (распакованные медиафайлы).
2. Запустить:

   ```bash
   docker compose -f compose.dev.yml up -d --build
   ```

3. Сайт: http://localhost:8081, админка: http://localhost:8081/admin/ (`admin` / `ozone`).
   Postgres доступен на `localhost:5433`, Django напрямую — `localhost:8000`.

Код из `./app` монтируется в контейнер, `runserver` перезапускается сам. Пересборка нужна только
при изменении `requirements.txt` или Dockerfile. Дамп заливается только в пустой том;
залить заново: `docker compose -f compose.dev.yml down -v && docker compose -f compose.dev.yml up -d`.

Полезное:

```bash
DEV=1 ./scripts/manage.sh test                                  # тесты
DEV=1 ./scripts/manage.sh makemessages -l be -l en              # строки для перевода
DEV=1 ./scripts/manage.sh compilemessages
```

## Продакшен

1. `cp .env.example .env` и заполнить (`DEBUG=False`, `SECRET_KEY`, хосты, пароли БД).
2. Сертификат в `./certs/globalsign.cer` (**полная цепочка**: сертификат + промежуточный) и `./certs/globalsign.key`.
3. Запуск / обновление:

   ```bash
   docker compose up -d --build      # первый запуск
   ./scripts/deploy.sh               # обновление: бэкап БД → git pull → сборка → перезапуск
   ```

При старте контейнера Django автоматически выполняются `migrate` и `collectstatic`.
Postgres наружу не публикуется.

### Бэкапы

```bash
./scripts/backup.sh                       # БД (.sql.gz) + медиа (.tar.gz) в ./backups, хранится 30 дней
./scripts/restore_db.sh backups/db_….sql.gz
```

Ежедневно через cron: `0 3 * * * cd /path/to/ozone-bsu && ./scripts/backup.sh >> backups/backup.log 2>&1`.
