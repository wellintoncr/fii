import orjson
import report_analyzer as analyzer

if __name__ == "__main__":
    # data_folder = "../reports_data"
    # all_data = analyzer.gather_all_reports(data_folder)
    # grouped_data = analyzer.group_all_reports(all_data)
    reports_data_file = '../reports_data/reports.json'
    result = analyzer.extract_id_isin_name(reports_data_file)
    names_relation_file = '../reports_data/names_relation.json'
    with open(names_relation_file, "w+") as file:
        file.write(orjson.dumps(result).decode())
    print(result)
