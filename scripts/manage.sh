#!/usr/bin/env bash
# Запуск manage.py в контейнере Django.
#   ./scripts/manage.sh createsuperuser
#   ./scripts/manage.sh makemessages -l be -l en && ./scripts/manage.sh compilemessages
#   DEV=1 ./scripts/manage.sh test          — в dev-окружении
set -euo pipefail
cd "$(dirname "$0")/.."

if [ "${DEV:-0}" = "1" ]; then COMPOSE="docker compose -f compose.dev.yml"; else COMPOSE=${COMPOSE:-"docker compose"}; fi
$COMPOSE exec django python manage.py "$@"
