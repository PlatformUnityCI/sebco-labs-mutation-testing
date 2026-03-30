import datetime
import pytest
from lib_core.time_utils.get_periods import GetPeriod
from lib_core.time_utils.date_utils import generate_time


@pytest.fixture
def response_json():
    account_created_date_str = "2024-11-27T13:36:44.071022997Z"

    account_created_date = datetime.datetime.fromisoformat(
        account_created_date_str.split("T")[0]
    ).date()

    today = datetime.datetime.fromisoformat(
        generate_time().split("T")[0]
    ).date()

    all_expected_periods = GetPeriod.get_expected_periods(
        account_created=account_created_date,
        today=today,
    )

    return {
        "accountCreatedDate": account_created_date_str,
        "periodList": all_expected_periods[:12],
    }
