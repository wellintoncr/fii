from datetime import datetime
from unittest import mock

from extractor.dividend_report import DividendReport

import pytest


def test_get_report_from_document_id_with_valid_response():
    with mock.patch("html_extractor.HTMLExtractor.get_raw_from_document_id") as mock_raw:
        with mock.patch("dividend_report.DividendReport.is_valid"):
            with open("tests/mocks/mock_dividend_report.html", "r") as file:
                to_return = file.readlines()
                mock_raw.return_value = "".join(to_return)
            dividend_report = DividendReport()
            response = dividend_report.get_report_from_document_id(1)
    expected = {
        "name": "FVPQ11",
        "isin_name": "BRFVPQCTF015",
        "dividend": 0.34,
        "payment_date": datetime(2021, 11, 9)
    }
    assert response == expected


def test_get_report_from_document_id_with_invalid_response():
    with mock.patch("html_extractor.HTMLExtractor.get_raw_from_document_id") as mock_raw:
        with mock.patch("extractor.dividend_report.DividendReport.is_valid") as is_valid_mock:
            is_valid_mock.return_value = False
            with open("tests/mocks/mock_dividend_report.html", "r") as file:
                to_return = file.readlines()
                mock_raw.return_value = "".join(to_return)
            dividend_report = DividendReport()
            with pytest.raises(Exception):
                dividend_report.get_report_from_document_id(1)
