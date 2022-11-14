import analyzer.report_analyzer as report_analyzer


def test_gather_all_reports():
    folder_name = "./tests/mocks"
    result = report_analyzer.gather_all_reports(folder_name)
    assert len(result["monthly_report"]) == 1
    assert result["monthly_report"][0]["document_id"] == 222222
    assert result["monthly_report"][0]["isin_name"] == "ISIN_MOCK"
    assert len(result["dividend_report"]) == 1
    assert result["dividend_report"][0]["document_id"] == 333333
    assert result["dividend_report"][0]["isin_name"] == "ISIN_MOCK"
