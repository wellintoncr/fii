from bs4 import BeautifulSoup
from datetime import datetime
import requests

class Monthly_Report:
    def __init__(self, base_url: str):
        self.__base_url = base_url
    
    def __extract_item(self, item: str, from_body=False) -> str:
        result = self.__raw_data.find(string=item)
        if result:
            return result.parent.parent.next_sibling.string
        raise ValueError("Item not found")

    def __format_item(self, item: str, format: str):
        if format == "float":
            return float(item.replace(".", "").replace(",", "."))
        elif format == "int":
            return int(float(item.replace(".", "").replace(",", ".")))
        return datetime.strptime(item, "%m/%Y")

    def __extract_all_data(self):
        valuation = self.__extract_item("Patrimônio Líquido – R$ ")
        amount_quotes = self.__extract_item("Número de Cotas Emitidas ")
        shareholder_quantity = self.__extract_item("Número de cotistas ")
        reference_date = self.__extract_item("Competência: ")
        output = {
            "name": self.__extract_item("Código ISIN: "),
            "valuation": self.__format_item(valuation, "float"),
            "amount_quotes": self.__format_item(amount_quotes, "int"),
            "shareholder_quantity": self.__format_item(shareholder_quantity, "int"),
            "reference_date": self.__format_item(reference_date, "datetime")
        }
        return output
    
    def __is_valid(self):
        header = self.__raw_data.find("h2")
        if header:
            return header.contents[0].lower() == "informe mensal"
        return False

    def get_report_from_document_id(self, document_id: int) -> dict:
        url = f"{self.__base_url}/fnet/publico/exibirDocumento?id={document_id}"
        headers = {"accept": "text/html"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise ValueError("This page is invalid")
        self.__raw_data = BeautifulSoup(response.text, "html.parser")
        if self.__is_valid():
            print(self.__extract_all_data())
            return None
        raise ValueError("This page content is invalid")

# HTTP because otherwise it would be necessary to deal with certificates
report = Monthly_Report("http://fnet.bmfbovespa.com.br")
report.get_report_from_document_id(237235)