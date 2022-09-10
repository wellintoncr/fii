from dividend_report import DividendReport
from monthly_report import MonthlyReport

if __name__ == "__main__":
    monthly_report = MonthlyReport()
    monthly_report.get_report_from_document_id(257165)
    dividend_report = DividendReport()
    dividend_report.get_report_from_document_id(272713)