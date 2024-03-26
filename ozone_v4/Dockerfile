FROM python:3.12-alpine

WORKDIR /ozone

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD echo 'Start Django:' \
    && sleep 7 \
    && python manage.py makemigrations \
    && python manage.py migrate \
#    && python manage.py collectstatic \
    && gunicorn config.wsgi:application --bind 0.0.0.0:8000