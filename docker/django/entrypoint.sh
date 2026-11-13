#!/bin/sh
# Общая точка входа dev/prod: ждём БД, применяем миграции, собираем статику.
set -e

echo "entrypoint: waiting for postgres at ${DB_HOST}:${DB_PORT}..."
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -q; do sleep 1; done

python manage.py migrate --noinput

if [ "$DEBUG" != "True" ]; then
  python manage.py collectstatic --noinput -v 0
fi

# dev: суперпользователь admin/ozone (только при DEBUG=True)
if [ "$DEBUG" = "True" ] && [ "${DEV_CREATE_ADMIN:-1}" = "1" ]; then
  python manage.py shell -c "from django.contrib.auth import get_user_model; U=get_user_model(); u,_=U.objects.get_or_create(username='admin'); u.is_staff=u.is_superuser=True; u.set_password('ozone'); u.save()"
fi

exec "$@"
