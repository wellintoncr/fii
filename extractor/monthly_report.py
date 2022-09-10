# Project related
from scrap_exceptions import PageContentInvalid, ItemNotFound
from html_extractor import HTMLExtractor

# External libraries
from bs4 import BeautifulSoup
from datetime import datetime
import re

class MonthlyReport:
    
    def __extract_item(self, item: str) -> str:
        """Extract one item where any text contain 'item'."""
        result = self.__raw_data.find(text=re.compile(item))
        if result:
            return result.parent.parent.next_sibling.string
        raise ItemNotFound(f"Item not found: {item}")

    def __format_item(self, item: str, format: str="datetime"):
        """Format 'item' to a defined type.
        Type accepts 'float', 'int', and datetime is the default behaviour.
        """
        if format == "float":
            return float(item.replace(".", "").replace(",", "."))
        elif format == "int":
            return int(float(item.replace(".", "").replace(",", ".")))
        return datetime.strptime(item, "%m/%Y")

    def __extract_all_data(self):
        """Combine all individual items into one dict."""
        valuation = self.__extract_item("Patrimônio Líquido")
        amount_quotes = self.__extract_item("Número de Cotas Emitidas")
        shareholder_quantity = self.__extract_item("Número de cotistas")
        reference_date = self.__extract_item("Competência:")
        output = {
            "isin_name": self.__extract_item("Código ISIN:"),
            "valuation": self.__format_item(valuation, "float"),
            "amount_quotes": self.__format_item(amount_quotes, "int"),
            "shareholder_quantity": self.__format_item(shareholder_quantity, "int"),
            "reference_date": self.__format_item(reference_date, "datetime")
        }
        return output
    
    def __is_valid(self):
        """Verify page to make sure it is valid."""
        header = self.__raw_data.find("h2")
        if header:
            return header.contents[0].lower() == "informe mensal"
        return False

    def get_report_from_document_id(self, document_id: int) -> dict:
        """Based on 'document_id', extract full report."""
        html_data = HTMLExtractor.get_raw_from_document_id(document_id)
        self.__raw_data = BeautifulSoup(html_data, "html.parser")
        if self.__is_valid():
            return self.__extract_all_data()
        raise PageContentInvalid("This page does not seem to be valid")
