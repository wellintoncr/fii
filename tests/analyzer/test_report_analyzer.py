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


def test_extract_id_isin_name():
    report_file = './tests/mocks/reports.json'
    result = report_analyzer.extract_id_isin_name(report_file)
    expected = {
        "XPIN11": "BRXPINCTF004",
        "BLMR11": "BRBLMRCTF002",
        "RBRM11": "BRRBRMCTF009",
    }
    assert result == expected
