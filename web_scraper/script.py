from concurrent.futures import ThreadPoolExecutor, as_completed

from html_extractor import HTMLExtractor

import orjson
import os

import scrap_exceptions as exc
from scraper import Scraper

batch_size = 1000

def first_report_id():
    raw_files_list = os.listdir("output/")
    reports_id = [int(each.split(".")[0]) for each in raw_files_list if ".json" in each]
    reports_id.sort(reverse=True)
    return reports_id[0] if reports_id else 200_000


with ThreadPoolExecutor() as executor:
    first_document_id = first_report_id()
    future_document = {
        executor.submit(HTMLExtractor.get_raw_from_document_id, document_id): document_id
        for document_id in range(first_document_id, first_document_id + batch_size + 1)
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
