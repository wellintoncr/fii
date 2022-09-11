from unittest import mock

from extractor.html_extractor import HTMLExtractor

import pytest


def test_get_report_from_document_id_with_valid_response():
    with mock.patch("requests.get") as requests_mock:
        requests_mock.return_value.status_code = 500
        with pytest.raises(Exception):
            HTMLExtractor.get_raw_from_document_id(1)

        requests_mock.return_value.status_code = 200
        requests_mock.return_value.headers = {"content-type": "pdf"}
        with pytest.raises(Exception):
            HTMLExtractor.get_raw_from_document_id(1)

        requests_mock.return_value.headers = {"content-type": "text/html"}
        assert HTMLExtractor.get_raw_from_document_id(1)
