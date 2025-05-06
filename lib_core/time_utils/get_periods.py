from datetime import datetime
from dateutil.relativedelta import relativedelta

# 👇 Este es el JSON de ejemplo, podrías pasarlo como fixture o parámetro si querés más flexibilidad.
response_json = {
    "accountCreatedDate": "2024-11-27T13:36:44.071022997Z",
    "periodList": [
        {
            "month": "3",
            "year": "2025",
            "title": "Marzo Reporte"
        },
        {
            "month": "2",
            "year": "2025",
            "title": "Febrero Reporte"
        },
        {
            "month": "1",
            "year": "2025",
            "title": "Enero Reporte"
        },
        {
            "month": "12",
            "year": "2024",
            "title": "Diciembre Reporte"
        },
        {
            "month": "11",
            "year": "2024",
            "title": "Noviembre Reporte"
        }
    ]
}

MONTHS = {
    "Enero": 1,
    "Febrero": 2,
    "Marzo": 3,
    "Abril": 4,
    "Mayo": 5,
    "Junio": 6,
    "Julio": 7,
    "Agosto": 8,
    "Septiembre": 9,
    "Octubre": 10,
    "Noviembre": 11,
    "Diciembre": 12,
}

REVERSE_MONTHS = {
    v: k for k, v in MONTHS.items()}

class GetPeriod:
    def __init__(self):
        pass

    @staticmethod
    def get_expected_periods(account_created, today_str):
        """
        :param account_created: Fecha de creación de la cuenta (formato ISO 8601 con hora)
        :param today_str: Fecha actual en formato YYYY-MM-DD
        :return: Lista de períodos mensuales esperados, desde la creación hasta el último período válido
        """
        # Convertir strings a objetos date
        today = datetime.fromisoformat(today_str).date()
        account_created_date = datetime.fromisoformat(account_created.split("T")[0]).date()

        # Evaluar si se debe incluir el mes pasado o el antepenúltimo
        is_after_fifth = today.day >= 5
        end_month = today.replace(day=1) if is_after_fifth else (today.replace(day=1) - relativedelta(months=1))

        start_month = account_created_date.replace(day=1)

        periods = []
        current = end_month - relativedelta(months=1)

        while current >= start_month:
            periods.append({
                "month": str(current.month),
                "year": str(current.year),
                "title": f"{REVERSE_MONTHS[current.month]} Reporte"
            })
            current -= relativedelta(months=1)

        return periods