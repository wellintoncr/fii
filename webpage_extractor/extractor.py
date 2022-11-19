import os

DEFAULT_DOCUMENT_ID = 200_000


def last_saved_report_id(folder_path: str):
    raw_files_list = os.listdir(folder_path)
    reports_id = [int(each.split(".")[0]) for each in raw_files_list if ".html" in each]
    reports_id.sort(reverse=True)
    return reports_id[0] if reports_id else DEFAULT_DOCUMENT_ID


def get_longest_run(failures_folder_path: str):
    raw_files_list = os.listdir(failures_folder_path)
    reports_id = [int(each.split(".")[0]) for each in raw_files_list if ".txt" in each]
    longest_run = 0
    reports_id.sort(reverse=True)
    reference = None
    for position, report_id in enumerate(reports_id):
        if position < len(reports_id) - 1 and report_id == reports_id[position + 1] + 1:
            longest_run += 1
            reference = report_id + 1
    return longest_run, reference
