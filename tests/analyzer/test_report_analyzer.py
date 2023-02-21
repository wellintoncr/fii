from datetime import date

import analyzer.report_analyzer as report_analyzer
import tests.mocks.reports as reports_mock


# def test_gather_all_reports():
#     folder_name = "./tests/mocks"
#     result = report_analyzer.gather_all_reports(folder_name)
#     assert len(result["monthly_report"]) == 1
#     assert result["monthly_report"][0]["document_id"] == 222222
#     assert result["monthly_report"][0]["isin_name"] == "ISIN_MOCK"
#     assert len(result["dividend_report"]) == 1
#     assert result["dividend_report"][0]["document_id"] == 333333
#     assert result["dividend_report"][0]["isin_name"] == "ISIN_MOCK"


def test_group_all_reports():
    result = report_analyzer.group_all_reports(reports_mock.REPORTS_GATHERED_RAW)
    assert result == reports_mock.REPORTS_GATHERED_EXPECTED


def test_gather_all_data():
    response = report_analyzer.gather_all_data(
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
    response = report_analyzer.get_same_month(reference=reference, target=payload)
    assert response == {
        "another_key": "another_value"
    }

    # Same month cannot be found
    del payload["2000-05-09"]
    response = report_analyzer.get_same_month(reference=reference, target=payload)
    assert response is None
