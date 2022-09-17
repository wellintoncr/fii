import re
from datetime import datetime

from scrap_exceptions import ItemNotFoundError


class DividendReport:

    def __init__(self, html_raw: str) -> None:
        self.html_raw = html_raw

    def extract_item(self, item: str, from_body=False) -> str:
        """Extract one item where any text contain 'item'."""
        result = self.html_raw.find(string=re.compile(item))
        if result:
            if from_body:
                return result.parent.parent.contents[2].string
            return result.parent.parent.next_sibling.string
        raise ItemNotFoundError(f"Item not found: {item}")  # pragma: no cover

    def format_item(self, item: str, format: str = "datetime") -> float or datetime:
        """Format 'item' to a defined type.
        Type accepts 'float' and datetime is the default behaviour.
        """
        if format == "float":
            return float(item.replace(".", "").replace(",", "."))
        return datetime.strptime(item, "%d/%m/%Y")

    def extract_all_data(self) -> dict:
        """Combine all individual items into one dict."""
        dividend = self.extract_item("Valor do provento", from_body=True)
        payment_date = self.extract_item("Data do pagamento", from_body=True)
        output = {
            "name": self.extract_item("Código de negociação"),
            "isin_name": self.extract_item("Código ISIN"),
            "dividend": self.format_item(dividend, "float"),
            "payment_date": self.format_item(payment_date, "datetime")
        }
        return output, None
