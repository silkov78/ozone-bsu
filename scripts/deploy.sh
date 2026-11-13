#!/usr/bin/env bash
# Обновление продакшена: бэкап БД → git pull → пересборка образа → перезапуск.
#   ./scripts/deploy.sh            — ветка по умолчанию (main)
#   BRANCH=redesign ./scripts/deploy.sh
set -euo pipefail
cd "$(dirname "$0")/.."

BRANCH=${BRANCH:-main}
[ -f .env ] || { echo "Нет файла .env (шаблон: .env.example)"; exit 1; }

./scripts/backup.sh db
git fetch --all --prune
git checkout "$BRANCH"
git pull --ff-only origin "$BRANCH"

docker compose build django
docker compose up -d            # миграции и collectstatic выполняются при старте контейнера
docker image prune -f >/dev/null

docker compose ps
echo "deploy: done ($(git rev-parse --short HEAD))"
