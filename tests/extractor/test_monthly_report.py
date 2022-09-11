from datetime import datetime
from unittest import mock

from extractor.monthly_report import MonthlyReport

import pytest


def test_get_report_from_document_id_with_valid_response():
    with mock.patch("html_extractor.HTMLExtractor.get_raw_from_document_id") as mock_raw:
        with mock.patch("monthly_report.MonthlyReport.is_valid"):
            with open("tests/mocks/mock_monthly_report.html", "r") as file:
                to_return = file.readlines()
                mock_raw.return_value = "".join(to_return)
            dividend_report = MonthlyReport()
            response = dividend_report.get_report_from_document_id(1)
    expected = {
        "amount_quotes": 111177,
        "isin_name": "BRALMICTF003",
        "valuation": 250264016.46,
        "reference_date": datetime(2021, 12, 1),
        "shareholder_quantity": 3154
    }
    assert response == expected


def test_get_report_from_document_id_with_invalid_response():
    with mock.patch("html_extractor.HTMLExtractor.get_raw_from_document_id") as mock_raw:
        with mock.patch("extractor.monthly_report.MonthlyReport.is_valid") as is_valid_mock:
            is_valid_mock.return_value = False
            with open("tests/mocks/mock_monthly_report.html", "r") as file:
                to_return = file.readlines()
                mock_raw.return_value = "".join(to_return)
            dividend_report = MonthlyReport()
            with pytest.raises(Exception):
                dividend_report.get_report_from_document_id(1)
