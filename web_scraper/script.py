import os
import orjson
from scraper import Scraper

WEBPAGES_PATH = "../webpages_dump"
REPORTS_DATA_PATH = "../reports_data"

webpages = os.listdir(WEBPAGES_PATH)
webpages = [each for each in webpages if ".html" in each]

output = []

for webpage in webpages:
    with open(f"{WEBPAGES_PATH}/{webpage}", "rb") as file:
        content = file.read().decode()
    document_id = int(webpage.split(".html")[0])
    scraper = Scraper(content, document_id=document_id)
    try:
        report_data = scraper.extract_report()
        if report_data["data"]:
            output.append(report_data)
        else:
            print(f"Something went wrong: {webpage}")
    except Exception as err:
        print(f"Something went wrong: {webpage} | {err}")
if output:
    with open(f"{REPORTS_DATA_PATH}/reports.json", "w+") as file:
        content = orjson.dumps(output)
        file.write(content.decode())
    result = Scraper.extract_id_isin_name(output)
    names_relation_file = f"{REPORTS_DATA_PATH}/names_relation.json"
    with open(names_relation_file, "w+") as file:
        file.write(orjson.dumps(result).decode())
