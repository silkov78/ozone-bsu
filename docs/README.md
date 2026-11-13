# Документация: редизайн сайта ННИЦ МО БГУ

Ветка `redesign-mockup`. Новый фронт перенесён из макета (`silkov78/ozone-new`) в Django-шаблоны,
бэкенд и структура БД — прежние (добавлено одно поле).

- [status.md](status.md) — что сделано и что осталось сделать
- [architecture.md](architecture.md) — архитектура и структура сайта

## Быстрый запуск (dev)

1. Положить в `local_data/` (папка в `.gitignore`):
   - `backup_*.sql` — дамп БД (берётся самый свежий по имени);
   - `media/` — распакованные медиафайлы (содержимое `_data/` из zip-архива медиа).
2. Запустить:

   ```bash
   docker compose -f compose.dev.yml up --build
   ```

3. Открыть http://localhost:8081 (Nginx) или http://localhost:8000 (Django напрямую).
   Админка: http://localhost:8081/admin/ — `admin` / `ozone` (пароль выставляется при каждом старте dev).

Дамп восстанавливается **только при создании нового тома** `postgres_data_redesign`.
Чтобы залить свежий дамп заново:

```bash
docker compose -f compose.dev.yml down && docker volume rm ozone-bsu_postgres_data_redesign
```

Порты: Postgres — `5433`, Django — `8000`, Nginx — `8081` (80 и 5432 на машине разработчика заняты).
