import requests


class HTMLExtractor:
    @staticmethod
    def get_raw_from_document_id(document_id: int, timeout=None):
        """Get page HTML based on 'document_id'.
        If the webserver returns something different from 200, raise PageLoadingError.
        'timeout', in seconds, define how long the request can wait until is cancelled.
        """
        base_url = "http://fnet.bmfbovespa.com.br"
        url = f"{base_url}/fnet/publico/exibirDocumento?id={document_id}"
        headers = {"accept": "text/html"}
        response = requests.get(url, headers=headers, timeout=timeout)
        if response.status_code == 200 and "text/html" in response.headers["content-type"]:
            return response.text
