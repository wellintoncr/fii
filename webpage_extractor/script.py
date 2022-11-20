from concurrent.futures import ThreadPoolExecutor, as_completed

import extractor as ext
import html_extractor as hext

batch_size = 1000
MAX_LONGEST_FAILURE_COUNTER = 1000

WEBPAGES_NOT_FOUND_PATH = "../webpages_not_found"
WEBPAGES_DUMP_PATH = "../webpages_dump"


longest_run, reference = ext.get_longest_run(WEBPAGES_NOT_FOUND_PATH)
if longest_run == MAX_LONGEST_FAILURE_COUNTER:
    print(f"""
        Longest consecutive failure counter reached ({longest_run}) at {reference}.
        You may increase this threshold or maybe there is no report beyond the last valid one
    """)
else:
    with ThreadPoolExecutor() as executor:
        first_document_id = ext.last_saved_report_id("..")
        future_document = {
            executor.submit(hext.get_raw_from_document_id, document_id): document_id
            for document_id in range(first_document_id, first_document_id + batch_size + 1)
        }
        for future in as_completed(future_document):
            document_id = future_document[future]
            print(f"Processing {document_id}")
            html_data = future.result()
            if html_data["content"]:
                with open(f"{WEBPAGES_DUMP_PATH}/{document_id}.html", "w+") as file:
                    file.write(html_data["content"])
            elif html_data["status"] == "success":
                with open(f"{WEBPAGES_NOT_FOUND_PATH}/{document_id}.txt", "w+") as file:
                    file.write("Not found")
