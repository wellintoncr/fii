from concurrent.futures import ThreadPoolExecutor, as_completed

from html_extractor import HTMLExtractor
import scrap_exceptions as exc
from scraper import Scraper

first_document_id = 257065
quantity_documents = 500

with ThreadPoolExecutor() as executor:
    future_document = {
        executor.submit(HTMLExtractor.get_raw_from_document_id, document_id): document_id
        for document_id in range(first_document_id, first_document_id + quantity_documents)
    }
    for future in as_completed(future_document):
        document_id = future_document[future]
        try:
            html_raw = future.result()
            scraper = Scraper(html_raw)
            report = scraper.extract_report()
            if report["report_type"]:
                print(report)
        except (exc.PageContentError, exc.PageLoadingError):
            pass
        except exc.ItemNotFoundError as err:
            print(err, document_id)
