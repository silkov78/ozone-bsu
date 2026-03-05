FROM python:3.12-alpine

WORKDIR /ozone

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apk add gettext

#COPY . .

CMD echo 'Start Django:' \
    && sleep 10 \
    && python manage.py makemigrations \
    && python manage.py migrate \
#    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', '', 'ozone')" \
#    && python manage.py collectstatic \
    && gunicorn config.wsgi:application --bind 0.0.0.0:8000
