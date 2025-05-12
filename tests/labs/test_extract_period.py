import datetime
import logging

import pytest
import json
from lib_core.time_utils.get_periods import GetPeriod
from lib_core.time_utils.get_periods import response_json
from lib_core.time_utils.date_utils import generate_time

@pytest.mark.regression
class TestExtractPeriods:
    def setup_method(self):
        self.today = generate_time().split('T')[0]

    def test_qa_reports(self):
        """
        Valida que, con el filtro vacío, el request solamente traiga
        datos del usuario ERA.
        """
        response = response_json # Acá va el servicio
        logging.info(json.dumps(response["periodList"], indent=4))

        actual_periods = response["periodList"]  # lista de dicts
        account_created_str = (response["accountCreatedDate"]).replace("Z", "")

        # Convertir a objetos datetime.date
        account_created = datetime.datetime.fromisoformat(account_created_str.split("T")[0]).date()
        today = datetime.datetime.fromisoformat(self.today).date()

        expected_periods = GetPeriod.get_expected_periods(account_created=account_created, today=today)

        #Validar cantidad esperada de reportes según si la fecha de creación es mayor a 1 año entonces debe mostrar 12 reportes
        if (today - account_created).days > 365:
            assert len(actual_periods) == 12, f"Se esperaban 12 reportes, pero se encontraron {len(actual_periods)}"
        else:
            #Validar si la cantidad de reportes es acorde entre lo actual y lo esperado ya que la cantidad a mostrar es menor a 12 por la validación anterior
            assert len(actual_periods) == len(expected_periods), (
                f"Cantidad de reportes incorrecta. Esperados: {len(expected_periods)}."
                f"Recibidos: {len(actual_periods)}"
            )

        #Validar orden descendente de títulos y fechas
        for expected, actual in zip(expected_periods, actual_periods):
            assert expected["month"] == actual["month"], f"Mes incorrecto: esperado {expected['month']}, recibido {actual['month']}"
            assert expected["year"] == actual["year"], f"Mes incorrecto: esperado {expected['year']}, recibido {actual['year']}"
            assert expected["title"] == actual["title"], f"Mes incorrecto: esperado {expected['title']}, recibido {actual['title']}"