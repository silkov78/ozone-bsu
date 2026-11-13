#!/bin/sh
# Первичное заполнение БД при создании нового тома postgres.
# Берёт самый свежий local_data/backup_*.sql (монтируется в /local_data).
set -e
DUMP=$(ls -1 /local_data/backup_*.sql 2>/dev/null | sort | tail -n 1 || true)
if [ -z "$DUMP" ]; then
  echo "initdb: дамп не найден в /local_data — пропускаю восстановление"
  exit 0
fi
echo "initdb: восстанавливаю $DUMP"
# в дампе владелец объектов — ozone_user
psql -v ON_ERROR_STOP=0 -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "DO \$\$BEGIN IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname='ozone_user') THEN CREATE ROLE ozone_user; END IF; END\$\$;"
psql -v ON_ERROR_STOP=1 -q -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f "$DUMP"
echo "initdb: готово"
