from concurrent.futures import ThreadPoolExecutor, as_completed

# from dividend_report import DividendReport
from monthly_report import MonthlyReport
import scrap_exceptions as exc

first_document_id = 257065
quantity_documents = 101

with ThreadPoolExecutor() as executor:
    monthly_report = MonthlyReport()
    future_document = {
        executor.submit(monthly_report.get_report_from_document_id, document_id): document_id
        for document_id in range(first_document_id, first_document_id + quantity_documents)
    }
    for future in as_completed(future_document):
        document_id = future_document[future]
        try:
            print(future.result())
        except (exc.PageContentError, exc.PageLoadingError) as err:
            print(f"Failed ({document_id}): {err}")
