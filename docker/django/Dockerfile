# Продакшен-образ: код копируется в образ, запуск через gunicorn
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# корпоративные корневые сертификаты (если есть) — для pip за прокси
COPY docker/django/certs/ /usr/local/share/local_certs/
RUN apk add --no-cache ca-certificates postgresql-client gettext \
 && find /usr/local/share/local_certs -name '*.pem' -exec cp {} /usr/local/share/ca-certificates/ \; \
 && update-ca-certificates

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .
COPY docker/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh \
 && addgroup -S django && adduser -S django -G django \
 && mkdir -p /app/staticfiles /app/media \
 && chown -R django:django /app

RUN mkdir -p /app/staticfiles && chown -R django:django /app/staticfiles
USER django
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
  CMD wget -qO- http://127.0.0.1:8000/healthz/ >/dev/null || exit 1

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "60", "--access-logfile", "-"]
