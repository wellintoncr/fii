from unittest import mock
from unittest.mock import MagicMock
import orjson
import pytest

import stock.stock_extractor as stock_extractor


def test_get_one():
    with open("tests/mocks/stock_prices.json", "rb") as stock_file:
        stock_mock_content = orjson.loads(stock_file.read())
    with open("tests/mocks/stock_prices_failure.json", "rb") as stock_file:
        stock_mock_failure_content = orjson.loads(stock_file.read())
    with open("tests/mocks/stock_prices_expected.json", "rb") as stock_expected:
        expected_content = orjson.loads(stock_expected.read())
    with mock.patch("requests.get") as get_mock:
        # Success
        get_mock.return_value = MagicMock(status_code=200, json=lambda: stock_mock_content)
        response = stock_extractor.get_one("SMTH11")
        assert response == expected_content

        # status 200 but something went wrong
        get_mock.return_value = MagicMock(status_code=200, json=lambda: stock_mock_failure_content)
        with pytest.raises(ValueError):
            stock_extractor.get_one("SMTH11")

        # Failure
        get_mock.return_value = MagicMock(status_code=500, json=lambda: "Server error")
        with pytest.raises(ValueError):
            stock_extractor.get_one("SMTH11")
