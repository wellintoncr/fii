import re
from datetime import datetime
from bs4 import BeautifulSoup

from html_extractor import HTMLExtractor
from scrap_exceptions import ItemNotFoundError, PageContentError


class DividendReport:

    def __extract_item(self, item: str, from_body=False) -> str:
        """Extract one item where any text contain 'item'."""
        result = self.__raw_data.find(text=re.compile(item))
        if result:
            if from_body:
                return result.parent.parent.contents[2].string
            return result.parent.parent.next_sibling.string
        raise ItemNotFoundError(f"Item not found: {item}")

    def __format_item(self, item: str, format: str = "datetime") -> float or datetime:
        """Format 'item' to a defined type.
        Type accepts 'float' and datetime is the default behaviour.
        """
        if format == "float":
            return float(item.replace(".", "").replace(",", "."))
        return datetime.strptime(item, "%d/%m/%Y")

    def __extract_all_data(self) -> dict:
        """Combine all individual items into one dict."""
        dividend = self.__extract_item("Valor do provento por cota", from_body=True)
        payment_date = self.__extract_item("Data do pagamento", from_body=True)
        output = {
            "name": self.__extract_item("Código de negociação da cota"),
            "isin_name": self.__extract_item("Código ISIN da cota"),
            "dividend": self.__format_item(dividend, "float"),
            "payment_date": self.__format_item(payment_date, "datetime")
        }
        return output

    def __is_valid(self) -> bool:
        """Verify page to make sure it is valid."""
        header = self.__raw_data.find("h1")
        if header:
            return header.contents[0].lower() == "informações sobre pagamento de proventos"
        return False

    def get_report_from_document_id(self, document_id: int) -> dict:
        """Based on 'document_id', extract full report."""
        html_data = HTMLExtractor.get_raw_from_document_id(document_id)
        self.__raw_data = BeautifulSoup(html_data, "html.parser")
        if self.__is_valid():
            return self.__extract_all_data()
        raise PageContentError("This page does not seem to be valid")
