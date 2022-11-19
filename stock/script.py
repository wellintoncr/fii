import stock_extractor

if __name__ == "__main__":
    response = stock_extractor.get_one("SPTW11")
    print(response)
