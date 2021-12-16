import requests
from scrap_exceptions import PageLoadingFailed

class HTML_Extractor:
    @staticmethod
    def get_raw_from_document_id(base_url: str, document_id: int):
        """Get page HTML based on 'document_id'."""
        url = f"{base_url}/fnet/publico/exibirDocumento?id={document_id}"
        headers = {"accept": "text/html"}
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code != 200:
            raise PageLoadingFailed(f"Invalid status: {response.status_code}")
        return response.text