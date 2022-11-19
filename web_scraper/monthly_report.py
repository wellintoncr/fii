import re
from datetime import datetime

from scrap_exceptions import ItemNotFoundError


class MonthlyReport:

    def __init__(self, html_raw: str) -> None:
        self.html_raw = html_raw

    def extract_item(self, item: str) -> str:
        """Extract one item where any text contain 'item'."""
        result = self.html_raw.find(string=re.compile(item))
        if result:
            return result.parent.parent.next_sibling.string
        raise ItemNotFoundError(f"Item not found: {item}")  # pragma: no cover

    def extract_type(self):
        """Extract fund type."""
        to_match = "Classificação autorregulação: "
        result = self.html_raw.find(string=re.compile(to_match))
        type_block = result.parent.parent.next_sibling
        output = {
            "mandato": type_block.find(string="Mandato: ").parent.parent.contents[1],
            "segmento": type_block.find(string="Segmento de Atuação: ").parent.parent.contents[1],
            "gestao": type_block.find(string="Tipo de Gestão: ").parent.parent.contents[1]
        }
        return {key: value.lower() for key, value in output.items()}

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
        has_deadline = self.extract_item("Prazo de Duração:")
        fund_type = self.extract_type()
        output = {
            "isin_name": self.extract_item("Código ISIN:"),
            "valuation": self.format_item(valuation, "float"),
            "amount_quotes": self.format_item(amount_quotes, "int"),
            "shareholder_quantity": self.format_item(shareholder_quantity, "int"),
            "reference_date": self.format_item(reference_date, "datetime"),
            "has_deadline": has_deadline != "Indeterminado",
            "type": fund_type
        }
        return output, None
