from bs4 import BeautifulSoup

from dividend_report import DividendReport
from monthly_report import MonthlyReport


class Scraper:

    def __init__(self, html_raw: str) -> None:
        self.html_raw = BeautifulSoup(html_raw, "html.parser")

    def get_report_type(self):
        """Get report type based on self.html_raw."""
        title = self.html_raw.find("title")
        valid_titles = {
            "anexo 39-i : informe mensal": "monthly_report",
            "informações sobre pagamento de proventos - fundos": "dividend_report"
        }
        return title and valid_titles.get(title.string.lower())

    def extract_report(self):
        """Extract one report from html_raw."""
        report_type = self.get_report_type()
        output = {
            "data": None,
            "error": None,
            "report_type": None
        }
        if report_type:
            output["report_type"] = report_type
            if report_type == "monthly_report":
                monthly_report = MonthlyReport(self.html_raw)
                data, error = monthly_report.extract_all_data()
            else:
                dividend_report = DividendReport(self.html_raw)
                data, error = dividend_report.extract_all_data()
            output["data"] = data
            output["error"] = error
        else:
            output["error"] = "unavailable"
        return output
