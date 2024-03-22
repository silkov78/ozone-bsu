# ozone-bsu

### Привет!
В данном репозитории располагается Django Fullstack проект для подразделения ННИЦ МО БГУ. Установите docker и docker-compose на вашу локальную машину
и в терминале введити команду docker-compose up.

#### Будут запущены следующие docker-контейнеры:
* ozone_nginx с настроенным web-сервера nginx 
* ozone_django_app с приложением Django и запущенным gunicorn
* ozone_postgres с БД для Django application