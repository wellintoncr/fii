import os
import orjson


def gather_all_reports(folder_name: str):
    files_list = [each for each in os.listdir(folder_name) if "json" in each]
    output = {
        "monthly_report": [],
        "dividend_report": []
    }
    for each in files_list:
        with open(f"{folder_name}/{each}", "rb") as file:
            content = orjson.loads(file.read())
        report_type = content.get("report_type")
        if report_type in ["monthly_report", "dividend_report"]:
            to_append = content["data"]
            to_append["document_id"] = int(each.split(".")[0])
            output[report_type].append(to_append)
    return output
