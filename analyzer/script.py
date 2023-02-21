import orjson

import report_analyzer as analyzer

if __name__ == "__main__":
    with open("../reports_data/reports.json", "rb") as file:
        reports_content = orjson.loads(file.read())
    with open("../reports_data/names_relation.json", "rb") as file:
        names_relation_content = orjson.loads(file.read())
    with open("../reports_data/stock_data.json", "rb") as file:
        stock_content = orjson.loads(file.read())

    # all_data = analyzer.gather_all_reports(data_folder)
    grouped_data = analyzer.gather_all_data(
        names_relation=names_relation_content,
        report_data=reports_content,
        stock_data=stock_content)
    with open("../reports_data/grouped_data.json", "w+") as output:
        output.write(orjson.dumps(grouped_data).decode())
