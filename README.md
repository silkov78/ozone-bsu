# ozone-bsu

Django Fullstack проект для подразделения ННИЦ МО БГУ.

Стек: Django + PostgreSQL + Nginx, всё поднимается через Docker Compose.
Есть два независимых набора конфигов:

* `compose.dev.yml` — для локальной разработки (Django `runserver` с автоперезагрузкой);
* `docker-compose.yml` — для продакшена (Django через `gunicorn`, HTTPS через Nginx).

---

## Локальный запуск (dev)

**Требования:** Docker, Docker Compose.

1. Убедитесь, что в `ozone_v4/.env.dev` заданы переменные окружения — файл уже
   лежит в репозитории с рабочими дефолтными значениями (креды тестовой БД,
   `DEBUG=True`), менять ничего не нужно для локального запуска.

2. Поднимите стек:

   ```bash
   docker compose -f compose.dev.yml up --build
   ```

   Поднимутся три контейнера:
   * `ozone_postgres_dev` — PostgreSQL, порт `5432`;
   * `ozone_django_app_dev` — Django (`manage.py runserver`), порт `8000`;
   * `ozone_nginx_dev` — Nginx-прокси перед Django, порт `80`.

3. Откройте **`http://localhost`** в браузере (не `:8000` — статика и медиа
   раздаются самим Django, но HTTP заголовки и проксирование эмулируют прод
   именно через Nginx).

4. При первом запуске автоматически:
   * накатятся миграции (`makemigrations` + `migrate`);
   * создастся суперпользователь `admin` / `ozone`, если его ещё нет.

5. Дальше просто редактируйте код — `runserver` сам перезагружается при
   изменении `.py`-файлов и шаблонов, пересобирать контейнер и делать
   `collectstatic` вручную не требуется. Пересборка (`--build`) нужна только
   если поменялся `requirements.txt` или сам `Dockerfile.dev`.

**Остановить:**

```bash
docker compose -f compose.dev.yml down
```

Данные Postgres и медиафайлы хранятся в именованных docker-volume'ах
(`postgres_data_dev`, `media_data_dev`) и переживают `down`/`up`. Чтобы
сбросить БД полностью — добавьте `-v`.

---

## Продакшен

**Требования:** Docker, Docker Compose, реальный SSL-сертификат для домена.

1. Заполните `ozone_v4/.env` реальными продовыми значениями (пример структуры
   смотрите в `ozone_v4/.env.dev`):

   ```
   DEBUG=False
   SECRET_KEY=<секретный ключ>
   ALLOWED_HOSTS='ozone.bsu.by www.ozone.bsu.by <ip сервера>'

   POSTGRES_USER=...
   POSTGRES_PASSWORD=...
   POSTGRES_DB=...

   DB_NAME=...
   DB_USER=...
   DB_PASSWORD=...
   DB_HOST=postgres
   DB_PORT=5432
   ```

   Этот файл в `.gitignore` и в репозиторий не коммитится.

2. Положите SSL-сертификат и ключ в `certs_2024/` — имена файлов должны
   совпадать с указанными в `conf/nginx_ozone.conf`
   (`globalsign2024.cer` / `globalsign2024.key`).

3. Поднимите стек:

   ```bash
   docker-compose up --build -d
   ```

   Контейнеры:
   * `ozone_postgres` — PostgreSQL, порт `5432`;
   * `ozone_django_app` — Django через `gunicorn`, порт `8000`;
   * `ozone_nginx` — Nginx с HTTPS (порты `80` → редирект на `443`, `443`).

4. Миграции (`makemigrations` + `migrate`) применяются автоматически при
   старте контейнера `django`. Сбор статики (`collectstatic`) в прод-образе
   не запускается автоматически — выполните его вручную после первого
   деплоя и после любых изменений в статических файлах:

   ```bash
   docker compose exec django python manage.py collectstatic --noinput
   ```

5. Приложение будет доступно по `https://ozone.bsu.by` (или по IP сервера).

**Остановить:**

```bash
docker-compose down
```

Данные Postgres, медиафайлы и собранная статика хранятся в именованных
volume'ах (`static_data`, `media_data`) и переживают перезапуск.
