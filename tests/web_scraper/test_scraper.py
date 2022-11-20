from datetime import datetime

from web_scraper.scraper import Scraper


def test_extract_invalid_page():
    with open("tests/mocks/mock_unavailable_page.html", "r") as file:
        html_raw = file.readlines()
        html_raw = "".join(html_raw)
    scraper = Scraper(html_raw)
    response = scraper.extract_report()
    assert response == {
        "report_type": None,
        "data": None,
        "error": "unavailable"
    }


def test_extract_monthly_report():
    with open("tests/mocks/mock_monthly_report.html", "r") as file:
        html_raw = file.readlines()
        html_raw = "".join(html_raw)
    scraper = Scraper(html_raw)
    response = scraper.extract_report()
    assert response == {
        "report_type": "monthly_report",
        "data": {
            "amount_quotes": 111177,
            "isin_name": "BRALMICTF003",
            "valuation": 250264016.46,
            "reference_date": datetime(2021, 12, 1),
            "shareholder_quantity": 3154,
            "has_deadline": False,
            "type": {
                "mandato": "renda",
                "segmento": "lajes corporativas",
                "gestao": "passiva"
            }
        },
        "error": None
    }


def test_extract_dividend_report():
    with open("tests/mocks/mock_dividend_report.html", "r") as file:
        html_raw = file.readlines()
        html_raw = "".join(html_raw)
    scraper = Scraper(html_raw)
    response = scraper.extract_report()
    assert response == {
        "report_type": "dividend_report",
        "data": {
            "name": "FVPQ11",
            "isin_name": "BRFVPQCTF015",
            "dividend": {
                "payment_date": datetime(2021, 11, 9),
                "amount": 0.34,
                "base_date": datetime(2021, 10, 29)
            },
            "amortization": {
                "payment_date": None,
                "amount": None,
                "base_date": None
            }
        },
        "error": None
    }


def test_extract_dividend_report_second_style():
    with open("tests/mocks/mock_dividend_report_second_style.html", "r") as file:
        html_raw = file.readlines()
        html_raw = "".join(html_raw)
    scraper = Scraper(html_raw)
    response = scraper.extract_report()
    expected = {
        "report_type": "dividend_report",
        "data": {
            "name": "XPIN11",
            "isin_name": "BRXPINCTF004",
            "dividend": {
                "payment_date": datetime(2022, 9, 23),
                "amount": 0.62,
                "base_date": datetime(2022, 9, 16)
            },
            "amortization": {
                "payment_date": None,
                "amount": None,
                "base_date": None
            }
        },
        "error": None
    }
    assert response == expected


def test_extract_dividend_report_with_amortization():
    with open("tests/mocks/dividend_report_with_amortization.html", "r") as file:
        html_raw = file.readlines()
        html_raw = "".join(html_raw)
    scraper = Scraper(html_raw)
    response = scraper.extract_report()
    expected = {
        "report_type": "dividend_report",
        "data": {
            "name": "KINP11",
            "isin_name": "BRKINPCTF001",
            "dividend": {
                "payment_date": datetime(2022, 11, 16),
                "amount": 0.136403050168062,
                "base_date": datetime(2022, 10, 31)
            },
            "amortization": {
                "payment_date": datetime(2022, 11, 18),
                "amount": 0.220343388733024,
                "base_date": datetime(2022, 10, 30)
            }
        },
        "error": None
    }
    assert response == expected


def test_get_report_type_with_valid_page():
    with open("tests/mocks/mock_monthly_report.html", "r") as file:
        html_raw = file.readlines()
        html_raw = "".join(html_raw)
    scraper = Scraper(html_raw)
    assert scraper.get_report_type() == "monthly_report"


def test_get_report_type_with_invalid_page():
    with open("tests/mocks/mock_unavailable_page.html", "r") as file:
        html_raw = file.readlines()
        html_raw = "".join(html_raw)
    scraper = Scraper(html_raw)
    assert scraper.get_report_type() is None
