from concurrent.futures import ThreadPoolExecutor, as_completed

from html_extractor import HTMLExtractor

import orjson

import scrap_exceptions as exc
from scraper import Scraper

first_document_id = 200000
last_document_id = 354000

with ThreadPoolExecutor() as executor:
    future_document = {
        executor.submit(HTMLExtractor.get_raw_from_document_id, document_id): document_id
        for document_id in range(first_document_id, last_document_id + 1)
    }
    for future in as_completed(future_document):
        document_id = future_document[future]
        if document_id % 100 == 0:
            print(f"Processing {document_id}")
        try:
            html_raw = future.result()
            scraper = Scraper(html_raw)
            report = scraper.extract_report()
            if report["report_type"]:
                with open(f"output/{document_id}.json", "w+") as file:
                    content = orjson.dumps(report).decode()
                    file.write(content)
        except exc.ItemNotFoundError as err:
            print("Failed", err, document_id)
        except Exception:
            pass
