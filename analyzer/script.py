import orjson

import report_analyzer as analyzer

if __name__ == "__main__":
    reports_data_folder = "../reports_data/reports.json"
    with open(reports_data_folder, "rb") as file:
        reports_content = orjson.loads(file.read())

    # all_data = analyzer.gather_all_reports(data_folder)
    grouped_data = analyzer.group_all_reports(reports_content)
    print(grouped_data)
