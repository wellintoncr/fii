import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from html_extractor import HTMLExtractor

import orjson

import scrap_exceptions as exc
from scraper import Scraper

batch_size = 1000
MAX_LONGEST_FAILURE_COUNTER = 1000


def first_report_id():
    raw_files_list = os.listdir("output/")
    reports_id = [int(each.split(".")[0]) for each in raw_files_list if ".json" in each]
    reports_id.sort(reverse=True)
    return reports_id[0] if reports_id else 200_000


def get_longest_run():
    raw_files_list = os.listdir("failures/")
    reports_id = [int(each.split(".")[1]) for each in raw_files_list if "not_found" in each]
    longest_run = 0
    reports_id.sort(reverse=True)
    reference = None
    for position, report_id in enumerate(reports_id):
        if position < len(reports_id) - 1:
            if report_id == reports_id[position + 1] + 1:
                longest_run += 1
                if longest_run >= MAX_LONGEST_FAILURE_COUNTER:
                    reference = report_id
                    break
            else:
                longest_run = 0
    return longest_run, reference


longest_run, reference = get_longest_run()
if longest_run == MAX_LONGEST_FAILURE_COUNTER:
    print(f"""
        Longest consecutive failure counter reached ({longest_run}) at {reference}.
        You may increase this threshold or maybe there is no report beyond the last valid one
    """)
else:
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
                else:
                    with open(f"failures/not_found.{document_id}.txt", "w+") as file:
                        file.write("Nothing to extract")
            except exc.ItemNotFoundError as err:
                with open(f"failures/{document_id}.txt", "w+") as file:
                    file.write(f"{err} || {document_id}")
            except Exception:
                pass
