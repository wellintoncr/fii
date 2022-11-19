import requests


def get_raw_from_document_id(document_id: int, timeout: int = None):
    """Get page HTML based on 'document_id'.
    Args:
        document_id: int - represents which document are about to get extracted
        timeout: int - defines how long the request can wait until it gets cancelled.
    Return:
        dict:
            {
                "status": "failed" or "success",
                "content": None or page content
            }
    """
    base_url = "http://fnet.bmfbovespa.com.br"
    url = f"{base_url}/fnet/publico/exibirDocumento?id={document_id}"
    headers = {"accept": "text/html"}
    response = requests.get(url, headers=headers, timeout=timeout)
    output = {
        "status": "failed",
        "content": None
    }
    if response.status_code == 200:
        output["status"] = "success"
        if "text/html" in response.headers.get("content-type", ""):
            content = response.text
            not_found_text = "<b>Esta informação não está disponível para visualização.</b>"
            is_not_found = not_found_text in content
            output["content"] = None if is_not_found else content
    return output
