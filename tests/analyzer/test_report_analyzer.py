from datetime import date

import organizer.gather_data as gather_data
import tests.mocks.reports as reports_mock


def test_gather_all_data():
    response = gather_data.gather_all_data(
        stock_data=reports_mock.STOCK_DATA_RAW,
        report_data=reports_mock.REPORT_DATA_RAW,
        names_relation=reports_mock.NAMES_RELATION_RAW
    )
    assert response == reports_mock.GATHER_ALL_DATA_EXPECTED


def test_get_same_month():
    # Same month is found
    reference = date(day=1, month=5, year=2000)
    payload = {
        "2000-02-15": {
            "key": "value"
        },
        "2000-05-09": {
            "another_key": "another_value"
        }
    }
    response = gather_data.get_same_month(reference=reference, target=payload)
    assert response == {
        "another_key": "another_value"
    }

    # Same month cannot be found
    del payload["2000-05-09"]
    response = gather_data.get_same_month(reference=reference, target=payload)
    assert response is None
