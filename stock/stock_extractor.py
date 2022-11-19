from copy import deepcopy
from datetime import datetime

import requests

import stock.config as config


def get_one(stock_name):
    stock_name_adapted = f"{stock_name}.SAO"
    url = f"{config.API_URL}&symbol={stock_name_adapted}&apikey={config.API_KEY}"
    response = requests.get(url=url)
    if response.status_code == 200:
        content = response.json()
        stock_prices = deepcopy(content["Monthly Time Series"])
        stock_date_to_delete = [
            each for each in stock_prices.keys() if datetime.strptime(each, "%Y-%m-%d")
        ]
        if stock_date_to_delete:
            stock_prices.pop(stock_date_to_delete[0])
        formatted_stock_prices = {}
        for date_key, prices in stock_prices.items():
            price = {}
            for each_key, each_price in prices.items():
                key = each_key.split(" ")[1]
                price[key] = each_price
            formatted_stock_prices[date_key] = price
        return {
            "name": stock_name,
            "stock_prices": formatted_stock_prices
        }
    raise ValueError(f"Something went wrong. Check error message: {response.json()}")
