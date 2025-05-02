from source.utils.datetime.get_periods import GetPeriod
from source.utils.datetime.schedule_date import ScheduleDate

@pytest.mark.regression
class TestExtractPeriods:
    def setup_method(self):
        self.new_formatted_date = ScheduleDate.get_customized_date(number_of_days=0)
        
    def test_qa_arg_available_months_service_filtered_by_ars_currency(self, debit_api_services, set_token_attribute_according_arg_user):
        """
        Valida que, con el filtro vacío, el request solamente traiga
        datos del usuario ERA.
        """
        response = # Falta acá obtener el json de response_json
        response_data = const.json.dumps(response, indent=4)
        print(response_data)

        account_created = (response["accountCreatedDate"]).replace("Z", "")
        today = self.new_formatted_date

        expected_periods = GetPeriod.get_expected_periods(account_created, today)
        actual_periods = response_data["periodList"]

        #Validar cantidad esperada
        if (today - account_created).days >= 365:
            assert len(actual_periods) == 12, f"Se esperaban 12 reportes, pero se encontraron {len(actual_periods)}"
        else:
            assert len(actual_periods) == len(expected_periods), (
                f"Cantidad de reportes incorrecta. Esperados: {len(expected_periods)}."
                f"Recibidos: {len(actual_periods)}"
            )

        #Validar orden descendente de títulos y fechas
        for expected, actual in zip(expected_periods, actual_periods):
            assert expected["month"] == actual["month"], f"Mes incorrecto: esperado {expected['month']}, recibido {actual['month']}"
            assert expected["year"] == actual["year"], f"Mes incorrecto: esperado {expected['year']}, recibido {actual['year']}"
            assert expected["title"] == actual["title"], f"Mes incorrecto: esperado {expected['title']}, recibido {actual['title']}"