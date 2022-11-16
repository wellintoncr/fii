import os
from copy import deepcopy
from datetime import datetime

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


def group_all_reports(all_reports: dict):
    output = {}
    all_data = deepcopy(all_reports["monthly_report"])
    all_data.extend(deepcopy(all_reports["dividend_report"]))
    for each in all_data:
        isin_name = each.pop("isin_name")
        if isin_name not in output.keys():
            output[isin_name] = {"name": None}
        if each.get("name"):
            output[isin_name]["name"] = each.pop("name")
        date = each.get("payment_date", each.get("reference_date"))
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        key = date.strftime("%m/%Y")
        if key not in output[isin_name].keys():
            output[isin_name][key] = {"dividend_report": [], "monthly_report": []}
        if each.get("dividend"):
            output[isin_name][key]["dividend_report"].append(each)
        else:
            output[isin_name][key]["monthly_report"].append(each)
    return output
