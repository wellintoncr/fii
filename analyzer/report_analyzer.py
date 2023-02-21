# import os
from copy import deepcopy
from datetime import date, datetime


# def gather_all_reports(folder_name: str):
#     files_list = [each for each in os.listdir(folder_name) if "json" in each]
#     output = {
#         "monthly_report": [],
#         "dividend_report": []
#     }
#     for each in files_list:
#         with open(f"{folder_name}/{each}", "rb") as file:
#             content = orjson.loads(file.read())
#         report_type = content.get("report_type")
#         if report_type in ["monthly_report", "dividend_report"]:
#             to_append = content["data"]
#             to_append["document_id"] = int(each.split(".")[0])
#             output[report_type].append(to_append)
#     return output


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


def get_same_month(reference: date, target: dict):
    for key, value in target.items():
        as_datetime = datetime.fromisoformat(key)
        if as_datetime.year == reference.year and as_datetime.month == reference.month:
            return deepcopy(value)


def gather_all_data(stock_data: list, report_data: list, names_relation: list) -> dict:
    output = {}
    for each_fund in stock_data:
        each_fund_name = each_fund["name"]
        isin_name = names_relation[each_fund_name]
        fund_report = list(filter(lambda item: item["data"]["isin_name"] == isin_name, report_data))
        fund_data = list(filter(lambda item: item["report_type"] == "monthly_report", fund_report))
        output[each_fund_name] = {}
        if fund_data:
            output[each_fund_name] = {
                "type": fund_data[0]["data"]["type"],
                "isin_name": fund_data[0]["data"]["isin_name"]
            }
        for report in fund_report:
            if report["report_type"] == "dividend_report":
                base_date = report["data"]["dividend"]["base_date"]
                base_date = base_date or report["data"]["amortization"]["base_date"]
                to_add = {
                    "dividend": report["data"]["dividend"],
                    "amortization": report["data"]["amortization"],
                }
            else:
                base_date = report["data"]["reference_date"]
                to_add = {
                    "valuation": report["data"]["valuation"],
                    "amount_quotes": report["data"]["amount_quotes"],
                    "shareholder_quantity": report["data"]["shareholder_quantity"]
                }
            base_date_as_date = datetime.fromisoformat(base_date).date()
            first_day = base_date_as_date.replace(day=1)
            first_day_as_str = first_day.strftime("%Y-%m-%d")
            stock_data = get_same_month(first_day, each_fund["stock_prices"])
            if stock_data:
                to_add["stock_prices"] = stock_data
            previous_data = output[each_fund_name].get(first_day_as_str, {})
            to_add = {**previous_data, **to_add}
            output[each_fund_name].update({first_day_as_str: to_add})
    return output
