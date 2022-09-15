import re
from datetime import datetime
from bs4 import BeautifulSoup

from html_extractor import HTMLExtractor
from scrap_exceptions import ItemNotFoundError, PageContentError


class MonthlyReport:

    def extract_item(self, item: str) -> str:
        """Extract one item where any text contain 'item'."""
        result = self.__raw_data.find(string=re.compile(item))
        if result:
            return result.parent.parent.next_sibling.string
        raise ItemNotFoundError(f"Item not found: {item}")  # pragma: no cover

    def format_item(self, item: str, format: str = "datetime"):
        """Format 'item' to a defined type.
        Type accepts 'float', 'int', and datetime is the default behaviour.
        """
        if format == "float":
            return float(item.replace(".", "").replace(",", "."))
        elif format == "int":
            return int(float(item.replace(".", "").replace(",", ".")))
        return datetime.strptime(item, "%m/%Y")

    def extract_all_data(self):
        """Combine all individual items into one dict."""
        valuation = self.extract_item("Patrimônio Líquido")
        amount_quotes = self.extract_item("Número de Cotas Emitidas")
        shareholder_quantity = self.extract_item("Número de cotistas")
        reference_date = self.extract_item("Competência:")
        output = {
            "isin_name": self.extract_item("Código ISIN:"),
            "valuation": self.format_item(valuation, "float"),
            "amount_quotes": self.format_item(amount_quotes, "int"),
            "shareholder_quantity": self.format_item(shareholder_quantity, "int"),
            "reference_date": self.format_item(reference_date, "datetime")
        }
        return output

    def is_valid(self):
        """Verify page to make sure it is valid."""
        header = self.__raw_data.find("h2")
        if header:
            return header.contents[0].lower() == "informe mensal"
        return False  # pragma: no cover

    def get_report_from_document_id(self, document_id: int) -> dict:
        """Based on 'document_id', extract full report."""
        html_data = HTMLExtractor.get_raw_from_document_id(document_id)
        self.__raw_data = BeautifulSoup(html_data, "html.parser")
        if self.is_valid():
            return self.extract_all_data()
        raise PageContentError("This page does not seem to be valid")
