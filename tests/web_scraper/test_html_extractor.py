from unittest import mock

from web_scraper.html_extractor import HTMLExtractor


def test_get_report_from_document_id_with_valid_response():
    with mock.patch("requests.get") as requests_mock:
        requests_mock.return_value.status_code = 500
        assert HTMLExtractor.get_raw_from_document_id(1) is None

        requests_mock.return_value.status_code = 200
        requests_mock.return_value.headers = {"content-type": "pdf"}
        assert HTMLExtractor.get_raw_from_document_id(1) is None

        requests_mock.return_value.headers = {"content-type": "text/html"}
        assert HTMLExtractor.get_raw_from_document_id(1)
