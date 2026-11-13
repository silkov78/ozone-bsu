from observations.models import Observations


class ObservationsInMatrix:
    """
    Класс ObservationsInMatrix подготавливает данные Observations
    к экспорту в CSV-файл на основе заполненной формы.
    """

    def __init__(self, form_values: dict, model: Observations):
        self.form_values = form_values
        self.model = model

    def filter_by_dates(self):
        """
        Метод filter_by_dates возвращает  отфильтрованный по датам queryset.
        Начальная и конечная даты задаются пользователем в форме.
        """

        start_date = self.form_values['start_date']
        end_date = self.form_values['end_date']

        queryset = self.model.objects.filter(
            date__gte=start_date,
            date__lte=end_date
        )

        return queryset

    def queryset_to_matrix(self, queryset):
        """
        Метод queryset_to_matrix преобразовывает заданный querysetв матрицу,
        которую удобно распарсить в CSV-файл. Также метод убирает поля,
        неуказанные в форме.
        """

        parameter = self.form_values['parameter']
        city = self.form_values['city']

        model_fields = [f.name for f in self.model._meta.get_fields()]
        fields_from_form = list(filter(
            lambda f: parameter in f and city in f or f == 'date',
            model_fields
        ))

        def add_measure_units(field_name):
            """
            Функция добавляет единицы измерения к полям в CSV-файле,
            сожержащие в себе 'common_ozone' и 'ground_ozone'.
            К полям 'date' и 'uvi' (измеряется в условных единицах)
            ничего добавлять не надо.
            """

            if "common_ozone" in field_name:
                return field_name + ', DU'
            elif "surface_ozone" in field_name:
                return field_name + ', ppb'
            return field_name

        filtered_data_matrix = [map(add_measure_units, fields_from_form)]
        filtered_data_matrix += list(queryset.values_list(*fields_from_form))

        return filtered_data_matrix

    def get_observations_matrix(self):
        """
        Метод использует функционал вышеописанных методов.
        Делает код более лаконичным.
        """

        filtered_by_date = self.filter_by_dates()
        observations_matrix = self.queryset_to_matrix(filtered_by_date)
        return observations_matrix


