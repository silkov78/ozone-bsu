from django import forms
from django.utils.translation import gettext_lazy as _


class ObservationsForm(forms.Form):
    CITIES = (
        ("", _("Все пункты")),
        ("minsk", _("Минск")),
        ("homel", _("Гомель")),
        ("naroch", _("Нарочь")),
    )

    PARAMETERS = (
        ("", _("Все параметры")),
        ("total_ozone", _("Общий озон")),
        ("surface_ozone", _("Приземный озон")),
        ("total_uvi", _("УФ-индекс")),
        ("max_uvi", _("УФ-макс")),
    )

    parameter = forms.ChoiceField(
        label=_("Параметры измерений:"),
        required=False,
        choices=PARAMETERS,
        widget=forms.Select(
            attrs={"class": "form-control"},
        )
    )

    city = forms.ChoiceField(
        label=_("Пункты измерений:"),
        required=False,
        choices=CITIES,
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )

    start_date = forms.DateField(
        label=_("Начальная дата:"),
        required=True,
        widget=forms.DateInput(
            format="%d-%m-%Y", 
            attrs={"type": "date", "class": "form-control"}
        ),
    )

    end_date = forms.DateField(
        label=_("Конечная дата:"),
        required=True,
        widget=forms.DateInput(
            format="%d-%m-%Y",
            attrs={"type": "date", "class": "form-control"}
        ),
    )
