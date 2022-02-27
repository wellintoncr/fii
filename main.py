from dividend_report import Dividend_Report
from monthly_report import Monthly_Report

if __name__ == "__main__":
    monthly_report = Monthly_Report()
    monthly_report.get_report_from_document_id(257165)
    dividend_report = Dividend_Report()
    dividend_report.get_report_from_document_id(272713)