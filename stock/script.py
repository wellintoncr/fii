import sys
import time
import orjson

sys.path.append("..")
import stock_extractor  # noqa: E402


if __name__ == "__main__":
    MIN_WAIT_TIME_SECONDS = 12
    names_relation_file = "../reports_data/names_relation.json"
    with open(names_relation_file, "rb") as file:
        names_relation = orjson.loads(file.read())
    all_names = names_relation.keys()
    stock_data_file = "../reports_data/stock_data.json"
    stock_data_failures_file = "../reports_data/stock_data_failures.json"
    all_stock_data = []
    all_stock_data_failures = []
    for name in all_names:
        try:
            print(f"Extracting: {name}")
            all_stock_data.append(stock_extractor.get_one(name))
            print("Cool down")
            time.sleep(MIN_WAIT_TIME_SECONDS)
        except Exception as err:
            error_data = {
                "name": name,
                "error": str(err)
            }
            all_stock_data_failures.append(error_data)
    with open(stock_data_file, "w+") as file:
        file.write(orjson.dumps(all_stock_data).decode())
    with open(stock_data_failures_file, "w+") as file:
        file.write(orjson.dumps(all_stock_data_failures).decode())
