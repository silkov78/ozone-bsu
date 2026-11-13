# Архитектура и структура сайта

## Общая схема

```
Браузер ──► Nginx (8081) ──► Django 4.2 (runserver / gunicorn) ──► PostgreSQL 16
                                   │
                                   ├─ шаблоны templates/  (серверный рендеринг, i18n RU/BE/EN)
                                   ├─ static/  (site.css, site.js, картинки, фавиконы)
                                   └─ media/   (фото новостей, сотрудников, приборов, отчёты, документы)
```

- Сайт рендерится на сервере (Django templates). JS только для интерактива: графики Chart.js,
  переключатели параметров, шапка. Данные наблюдений передаются в страницу через `json_script`.
- Мультиязычность: `django-modeltranslation` для полей моделей (`*_ru/_be/_en`, fallback на ru),
  `{% trans %}` + `locale/` для интерфейса, русский — без префикса в URL, `/be/…`, `/en/…`.
- Админка Django — единственный инструмент наполнения. Тексты — CKEditor 5, наблюдения — django-import-export.

## Приложения Django

| Приложение | Модели | Что отдаёт |
|---|---|---|
| `main_app` | `News`, `Article` (+`ArticleFile`), `Devices` (+`DevicesCharacteristic`), `Document`, `AnnualReport` | главная, новости, о центре, прибор, статья, документы, поиск |
| `observations` | `Observations` — одна строка на дату, столбцы `{total_ozone,total_uvi,max_uvi}_{minsk,homel,naroch}`, `surface_ozone_minsk` | страница наблюдений, выгрузка CSV/XLSX, JSON-API |
| `staff` | `Worker` (+`Education`, `Career`, `Reward`, `ScienceInterest`, `Publication`) | страница сотрудника, JSON-API |

Шаблонные фильтры — `main_app/templatetags/site_tags.py`: `rich_text`, `excerpt`, `domain`, `file_ext`, `safe_size`.

## Структура сайта (URL)

| URL | Страница | Шаблон |
|---|---|---|
| `/` | Главная: hero с данными трёх станций, 3 последние новости, блок «О центре» | `index.html` |
| `/observations/` | Наблюдения: «Что мы измеряем», график по городу, последние данные, выгрузка | `observations.html` |
| `/observations/export/` | Выгрузка CSV/XLSX (`from`, `to`, `format`) | — |
| `/observations/chart-data/` | JSON-API (Минск, `range=week|month|year|all`) | — |
| `/news/`, `/news/<id>/` | Новости: сетка 3:2 с пагинацией; страница новости с источником | `news.html`, `news-item.html` |
| `/about/` | О центре: общая информация, подразделения, сотрудники, приборы, научная деятельность, годовые отчёты (якоря) | `about.html` |
| `/staff/<id>/` | Сотрудник | `team-member.html` |
| `/devices/<id>/` | Прибор с характеристиками | `device.html` |
| `/articles/<id>/` | Статья с файлами | `article.html` |
| `/documents/` | Документы | `documents.html` |
| `/search/?q=` | Поиск по новостям | `search.html` |
| `/cookies/` | Политика конфиденциальности | `cookies.html` |
| `/admin/` | Админка | — |
| `/api/staff/v1/workers/…` | JSON-API сотрудников (вне языковых префиксов) | — |

Редиректы 301: `/blog/…` → `/news/…`, `/observations/info|download/` → `/observations/`,
`/staff/` → `/about/#team`, `/articles/` → `/about/#science`, `/devices/` → `/about/#devices`.

## Файлы фронта

```
ozone_v4/
├── templates/
│   ├── base.html            шапка (меню, RU/BE/EN), подвал, подключение css/js
│   ├── partials/news_card.html
│   └── *.html               страницы (см. таблицу)
└── static/
    ├── css/site.css         все стили (палитра: #1e4356, #68a4c4, #0091c2, #a2cce3, #f3f8fa)
    ├── js/site.js           даты, уровни УФ, lastOf(), анимация графиков, шапка, версия для слабовидящих, cookie
    ├── css/fonts.css, fonts/manrope/   шрифт Manrope (локально)
    ├── vendor/chartjs/      Chart.js 4.4.1 (локально)
    └── img/site/, img/brand/  фон, фото здания, фавиконы
```

## Данные и окружение

- `local_data/` (не в git): `backup_*.sql`, медиа-архив и `media/`, выгрузки xlsx.
- `docker/initdb/00-restore.sh`: при создании тома Postgres восстанавливает самый свежий дамп
  (создаёт роль `ozone_user` — владельца объектов в дампе).
- Наблюдения Гомеля и Нарочи приходят с задержкой ~неделю: фронт везде берёт последнюю
  **непустую** дату по каждому пункту (`lastOf`), периоды графиков отсчитываются от неё.
