# import os
from copy import deepcopy
from datetime import date, datetime


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
