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
    scraper = Scraper(content)
    report_data = scraper.extract_report()
    if report_data["data"]:
        output.append(report_data)
    else:
        print(f"Something went wrong: {webpage}")
if output:
    with open(f"{REPORTS_DATA_PATH}/reports.json", "w+") as file:
        content = orjson.dumps(output)
        file.write(content.decode())
