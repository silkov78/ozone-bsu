#!/usr/bin/env bash
# Бэкап БД и медиафайлов продакшена в ./backups (хранится KEEP_DAYS дней).
#   ./scripts/backup.sh               — БД + медиа
#   ./scripts/backup.sh db            — только БД
# Для cron:  0 3 * * *  cd /path/to/ozone-bsu && ./scripts/backup.sh >> backups/backup.log 2>&1
set -euo pipefail
cd "$(dirname "$0")/.."

COMPOSE=${COMPOSE:-"docker compose"}
KEEP_DAYS=${KEEP_DAYS:-30}
TS=$(date +%Y%m%d_%H%M)
mkdir -p backups

echo "[$(date '+%F %T')] backup: database"
$COMPOSE exec -T postgres sh -c 'pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" --no-owner' \
  | gzip > "backups/db_${TS}.sql.gz"

if [ "${1:-all}" != "db" ]; then
  echo "[$(date '+%F %T')] backup: media"
  $COMPOSE exec -T django tar -C /app -czf - media > "backups/media_${TS}.tar.gz"
fi

find backups -name 'db_*.sql.gz' -mtime +"$KEEP_DAYS" -delete
find backups -name 'media_*.tar.gz' -mtime +"$KEEP_DAYS" -delete
echo "[$(date '+%F %T')] backup: done -> backups/*_${TS}.*"
