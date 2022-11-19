from unittest import mock

import webpage_extractor.html_extractor as hext


def test_get_report_from_document_id_with_valid_response():
    with open("tests/mocks/mock_unavailable_page.html", "rb") as unavailable_page:
        unavailable_content = unavailable_page.read().decode()
    with open("tests/mocks/mock_dividend_report.html", "rb") as available_page:
        available_content = available_page.read().decode()
    with mock.patch("requests.get") as requests_mock:
        requests_mock.return_value.status_code = 500
        expected = {"status": "failed", "content": None}
        assert hext.get_raw_from_document_id(1) == expected

        requests_mock.return_value.status_code = 200
        requests_mock.return_value.headers = {"content-type": "pdf"}
        expected = {"status": "success", "content": None}
        assert hext.get_raw_from_document_id(1) == expected

        requests_mock.return_value.headers = {"content-type": "text/html"}
        requests_mock.return_value.text = unavailable_content
        expected = {"status": "success", "content": None}
        assert hext.get_raw_from_document_id(1) == expected

        requests_mock.return_value.text = available_content
        expected = {"status": "success", "content": available_content}
        assert hext.get_raw_from_document_id(1) == expected
