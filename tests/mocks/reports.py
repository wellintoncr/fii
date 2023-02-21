STOCK_DATA_RAW = [
    {
        "name": "SMTH11",
        "stock_prices": {
            "2022-03-31": {
                "open": "92.0400",
                "high": "93.7600",
                "low": "90.5700",
                "close": "91.7200",
                "volume": "1085214"
            }
        }
    },
    {
        "name": "SMTE11",
        "stock_prices": {
            "2021-08-31": {
                "open": "12.0400",
                "high": "23.7600",
                "low": "11.5700",
                "close": "15.7200",
                "volume": "852333"
            }
        }
    }
]

NAMES_RELATION_RAW = {
    "SMTH11": "BRSMTH11MMM",
    "SMTE11": "BRSMTE11LLL"
}

REPORT_DATA_RAW = [
    {
        "data": {
            "name": "SMTH11",
            "isin_name": "BRSMTH11MMM",
            "dividend": {
                "amount": 1.220111732,
                "payment_date": "2022-03-17T00:00:00",
                "base_date": "2022-03-10T00:00:00"
            },
            "amortization": {
                "amount": None,
                "payment_date": None,
                "base_date": None
            },
            "document_id": 275492
        },
        "error": None,
        "report_type": "dividend_report"
    },
    {
        "data": {
            "isin_name": "BRSMTH11MMM",
            "valuation": 473865656.55,
            "amount_quotes": 4634191,
            "shareholder_quantity": 28814,
            "reference_date": "2022-03-01T00:00:00",
            "has_deadline": False,
            "type": {
                "mandato": "títulos e valores mobiliários",
                "segmento": "títulos e val. mob.",
                "gestao": "ativa"
            },
            "document_id": 215711
        },
        "error": None,
        "report_type": "monthly_report"
    },
    {
        "data": {
            "isin_name": "BRSMTE11LLL",
            "valuation": 473865656.55,
            "amount_quotes": 4634191,
            "shareholder_quantity": 28814,
            "reference_date": "2021-08-01T00:00:00",
            "has_deadline": False,
            "type": {
                "mandato": "títulos e valores mobiliários",
                "segmento": "títulos e val. mob.",
                "gestao": "ativa"
            },
            "document_id": 215711
        },
        "error": None,
        "report_type": "monthly_report"
    },
    {
        "data": {
            "name": "SMTE11",
            "isin_name": "BRSMTE11LLL",
            "dividend": {
                "amount": None,
                "payment_date": None,
                "base_date": None
            },
            "amortization": {
                "amount": 1.220111732,
                "payment_date": "2021-08-17T00:00:00",
                "base_date": "2021-08-10T00:00:00"
            },
            "document_id": 275492
        },
        "error": None,
        "report_type": "dividend_report"
    },
]

GATHER_ALL_DATA_EXPECTED = {
    "SMTH11": {
        "type": {
            "mandato": "títulos e valores mobiliários",
            "segmento": "títulos e val. mob.",
            "gestao": "ativa"
        },
        "isin_name": "BRSMTH11MMM",
        "2022-03-01": {
            "dividend": {
                "amount": 1.220111732,
                "payment_date": "2022-03-17T00:00:00",
                "base_date": "2022-03-10T00:00:00"
            },
            "amortization": {
                "amount": None,
                "payment_date": None,
                "base_date": None
            },
            "valuation": 473865656.55,
            "amount_quotes": 4634191,
            "shareholder_quantity": 28814,
            "stock_prices": {
                "open": "92.0400",
                "high": "93.7600",
                "low": "90.5700",
                "close": "91.7200",
                "volume": "1085214"
            }
        }
    },
    "SMTE11": {
        "isin_name": "BRSMTE11LLL",
        "type": {
            "mandato": "títulos e valores mobiliários",
            "segmento": "títulos e val. mob.",
            "gestao": "ativa"
        },
        "2021-08-01": {
            "dividend": {
                "amount": None,
                "payment_date": None,
                "base_date": None
            },
            "amortization": {
                "amount": 1.220111732,
                "payment_date": "2021-08-17T00:00:00",
                "base_date": "2021-08-10T00:00:00"
            },
            "valuation": 473865656.55,
            "amount_quotes": 4634191,
            "shareholder_quantity": 28814,
            "stock_prices": {
                "open": "12.0400",
                "high": "23.7600",
                "low": "11.5700",
                "close": "15.7200",
                "volume": "852333"
            }
        }
    }
}
