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

    def extract_dividend(self):
        """Extract dividend (dividend itself and amortization)."""
        amortization = None
        result = self.html_raw.find(string=re.compile("Valor do provento"))
        dividend = result.parent.parent.contents[2].string
        amortization = result.parent.parent.contents[3].string
        return {"dividend": dividend, "amortization": amortization}

    def format_item(self, item: str, format: str = "datetime") -> float or datetime:
        """Format 'item' to a defined type.
        Type accepts 'float' and datetime is the default behaviour.
        """
        if not item:
            return None
        if format == "float":
            return float(item.replace(".", "").replace(",", "."))
        return datetime.strptime(item, "%d/%m/%Y")

    def extract_all_data(self) -> dict:
        """Combine all individual items into one dict."""
        payment_date = self.extract_item("Data do pagamento", from_body=True)
        dividends = self.extract_dividend()
        output = {
            "name": self.extract_item("Código de negociação"),
            "isin_name": self.extract_item("Código ISIN"),
            "dividend": self.format_item(dividends["dividend"], "float"),
            "payment_date": self.format_item(payment_date, "datetime"),
            "amortization_dividend": self.format_item(dividends["amortization"], "float")
        }
        return output, None
