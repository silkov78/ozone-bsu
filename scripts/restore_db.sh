#!/usr/bin/env bash
# Восстановление БД из дампа (.sql или .sql.gz). ВНИМАНИЕ: текущие данные будут удалены.
#   ./scripts/restore_db.sh backups/db_20261113_0300.sql.gz
#   COMPOSE="docker compose -f compose.dev.yml" ./scripts/restore_db.sh local_data/backup_20261112.sql
set -euo pipefail
cd "$(dirname "$0")/.."

FILE=${1:?Укажите файл дампа: ./scripts/restore_db.sh <file.sql[.gz]>}
COMPOSE=${COMPOSE:-"docker compose"}

read -r -p "Все данные в БД будут заменены дампом $FILE. Продолжить? [y/N] " ok
[ "$ok" = "y" ] || { echo "Отменено"; exit 1; }

$COMPOSE stop django
$COMPOSE exec -T postgres sh -c 'psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"'
if [[ "$FILE" == *.gz ]]; then gunzip -c "$FILE"; else cat "$FILE"; fi \
  | $COMPOSE exec -T postgres sh -c 'psql -q -U "$POSTGRES_USER" -d "$POSTGRES_DB"'
$COMPOSE start django   # при старте применятся недостающие миграции
echo "restore: done"
