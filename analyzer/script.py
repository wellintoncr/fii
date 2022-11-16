import report_analyzer as analyzer

if __name__ == "__main__":
    data_folder = "../output"
    all_data = analyzer.gather_all_reports(data_folder)
    grouped_data = analyzer.group_all_reports(all_data)
    print(grouped_data)
