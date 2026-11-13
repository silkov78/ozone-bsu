import csv
from datetime import date, timedelta

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Observations

# порядок столбцов в выгрузке и в JSON для графиков
FIELDS = [
    'total_ozone_minsk', 'total_uvi_minsk', 'max_uvi_minsk', 'surface_ozone_minsk',
    'total_ozone_homel', 'total_uvi_homel', 'max_uvi_homel',
    'total_ozone_naroch', 'total_uvi_naroch', 'max_uvi_naroch',
]


def observations_json(days=None):
    """Наблюдения для графиков: [{date, total_ozone_minsk, ...}, ...] по возрастанию даты.
    days — сколько последних дней (от последней даты в БД); None — все."""
    qs = Observations.objects.order_by('date')
    if days:
        last = qs.last()
        if last:
            qs = qs.filter(date__gte=last.date - timedelta(days=days))
    return [
        {'date': o['date'].isoformat(), **{f: o[f] for f in FIELDS}}
        for o in qs.values('date', *FIELDS)
    ]


def observations_page(request):
    """Страница наблюдений: график по городу, последние данные, выгрузка."""
    return render(request, 'observations.html', {'observations': observations_json()})


def _parse_date(value, default):
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        return default


def observations_export(request):
    """Выгрузка всех пунктов и параметров за период: ?from=YYYY-MM-DD&to=YYYY-MM-DD&format=csv|xlsx"""
    qs = Observations.objects.order_by('date')
    first, last = qs.first(), qs.last()
    if not first:
        return HttpResponse(status=404)
    d_from = _parse_date(request.GET.get('from'), first.date)
    d_to = _parse_date(request.GET.get('to'), last.date)
    rows = qs.filter(date__gte=d_from, date__lte=d_to).values_list('date', *FIELDS)
    header = ['date', *FIELDS]
    filename = f'observations_{d_from}_{d_to}'

    if request.GET.get('format') == 'xlsx':
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        ws.title = 'observations'
        ws.append(header)
        for r in rows:
            ws.append(list(r))
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{filename}.xlsx"'
        wb.save(response)
        return response

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
    writer = csv.writer(response)
    writer.writerow(header)
    writer.writerows(rows)
    return response


def observations_chart_data(request):
    """JSON-API (оставлен для совместимости): данные Минска за неделю/месяц/год/всё."""
    days = {'week': 7, 'month': 30, 'year': 365, 'all': None}.get(request.GET.get('range', 'week'), 7)
    data = observations_json(days)
    if not data:
        return JsonResponse({'error': 'No observations found'}, status=404)
    return JsonResponse({
        'labels': [o['date'] for o in data],
        'total_ozone': [o['total_ozone_minsk'] for o in data],
        'surface_ozone': [o['surface_ozone_minsk'] for o in data],
        'uvi': [o['total_uvi_minsk'] for o in data],
        'uvi_max': [o['max_uvi_minsk'] for o in data],
    })
