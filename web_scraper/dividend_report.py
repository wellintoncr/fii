import re
from datetime import datetime

from scrap_exceptions import ItemNotFoundError


class DividendReport:

    def __init__(self, html_raw: str) -> None:
        self.html_raw = html_raw

    def extract_item(self, item: str) -> str:
        """Extract one item where any text contain 'item'."""
        result = self.html_raw.find(string=re.compile(item))
        if result:
            return result.parent.parent.next_sibling.string
        raise ItemNotFoundError(f"Item not found: {item}")  # pragma: no cover

    def extract_dividend(self):
        """Extract dividend (dividend itself and amortization)."""
        amortization = {}
        dividend = {}
        income_line = self.html_raw.find(string=re.compile("Valor do provento"))
        base_date_line = self.html_raw.find(string=re.compile("Data-base"))
        payment_date_line = self.html_raw.find(string=re.compile("Data do pagamento"))

        dividend["amount"] = self.format_item(
            income_line.parent.parent.contents[2].string, 'float')
        dividend["payment_date"] = self.format_item(
            payment_date_line.parent.parent.contents[2].string, 'datetime')
        dividend["base_date"] = self.format_item(
            base_date_line.parent.parent.contents[2].string, 'datetime')

        amortization["amount"] = self.format_item(
            income_line.parent.parent.contents[3].string, 'float')
        amortization["payment_date"] = self.format_item(
            payment_date_line.parent.parent.contents[3].string, 'datetime')
        amortization["base_date"] = self.format_item(
            base_date_line.parent.parent.contents[3].string, 'datetime')

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
        dividends = self.extract_dividend()
        output = {
            "name": self.extract_item("Código de negociação"),
            "isin_name": self.extract_item("Código ISIN"),
        }
        return dict(**output, **dividends), None
