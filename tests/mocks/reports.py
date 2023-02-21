REPORTS_GATHERED_RAW = {
    "monthly_report": [
        {
            "isin_name": "ISIN_MOCK",
            "valuation": 9999.52,
            "amount_quotes": 200,
            "shareholder_quantity": 30,
            "reference_date": "2020-12-01T00:00:00",
            "document_id": 222222
        },
        {
            "isin_name": "ISIN_MOCK",
            "valuation": 5555.52,
            "amount_quotes": 200,
            "shareholder_quantity": 30,
            "reference_date": "2022-10-12T00:00:00",
            "document_id": 333333
        },
        {
            "isin_name": "ISIN_MOCK",
            "valuation": 11111.52,
            "amount_quotes": 200,
            "shareholder_quantity": 30,
            "reference_date": "2021-09-12T00:00:00",
            "document_id": 444444
        }
    ],
    "dividend_report": [
        {
            "isin_name": "ISIN_MOCK",
            "name": "SMTH11",
            "dividend": 0.99,
            "payment_date": "2020-12-15T00:00:00",
            "document_id": 888888
        },
        {
            "isin_name": "ISIN_MOCK",
            "name": "SMTH11",
            "dividend": 0.55,
            "payment_date": "2022-10-07T00:00:00",
            "document_id": 999999
        },
        {
            "isin_name": "ISIN_MOCK_SECOND",
            "name": "SMEL11",
            "dividend": 0.22,
            "payment_date": "2022-10-07T00:00:00",
            "document_id": 999999
        }
    ]
}

REPORTS_GATHERED_EXPECTED = {
    "ISIN_MOCK": {
        "name": "SMTH11",
        "12/2020": {
            "dividend_report": [
                {
                    "document_id": REPORTS_GATHERED_RAW["dividend_report"][0]["document_id"],
                    "dividend": REPORTS_GATHERED_RAW["dividend_report"][0]["dividend"],
                    "payment_date": REPORTS_GATHERED_RAW["dividend_report"][0]["payment_date"]
                }
            ],
            "monthly_report": [
                {
                    "document_id": REPORTS_GATHERED_RAW["monthly_report"][0]["document_id"],
                    "valuation": REPORTS_GATHERED_RAW["monthly_report"][0]["valuation"],
                    "amount_quotes": REPORTS_GATHERED_RAW["monthly_report"][0]["amount_quotes"],
                    "shareholder_quantity":
                    REPORTS_GATHERED_RAW["monthly_report"][0]["shareholder_quantity"],
                    "reference_date": REPORTS_GATHERED_RAW["monthly_report"][0]["reference_date"]
                }
            ]
        },
        "10/2022": {
            "dividend_report": [
                {
                    "document_id": REPORTS_GATHERED_RAW["dividend_report"][1]["document_id"],
                    "dividend": REPORTS_GATHERED_RAW["dividend_report"][1]["dividend"],
                    "payment_date": REPORTS_GATHERED_RAW["dividend_report"][1]["payment_date"]
                }
            ],
            "monthly_report": [
                {
                    "document_id": REPORTS_GATHERED_RAW["monthly_report"][1]["document_id"],
                    "valuation": REPORTS_GATHERED_RAW["monthly_report"][1]["valuation"],
                    "amount_quotes": REPORTS_GATHERED_RAW["monthly_report"][1]["amount_quotes"],
                    "shareholder_quantity":
                    REPORTS_GATHERED_RAW["monthly_report"][1]["shareholder_quantity"],
                    "reference_date": REPORTS_GATHERED_RAW["monthly_report"][1]["reference_date"]
                }
            ]
        },
        "09/2021": {
            "dividend_report": [],
            "monthly_report": [
                {
                    "document_id": REPORTS_GATHERED_RAW["monthly_report"][2]["document_id"],
                    "valuation": REPORTS_GATHERED_RAW["monthly_report"][2]["valuation"],
                    "amount_quotes": REPORTS_GATHERED_RAW["monthly_report"][2]["amount_quotes"],
                    "shareholder_quantity":
                    REPORTS_GATHERED_RAW["monthly_report"][2]["shareholder_quantity"],
                    "reference_date": REPORTS_GATHERED_RAW["monthly_report"][2]["reference_date"]
                }
            ]
        }
    },
    "ISIN_MOCK_SECOND": {
        "name": "SMEL11",
        "10/2022": {
            "dividend_report": [
                {
                    "document_id": REPORTS_GATHERED_RAW["dividend_report"][2]["document_id"],
                    "dividend": REPORTS_GATHERED_RAW["dividend_report"][2]["dividend"],
                    "payment_date": REPORTS_GATHERED_RAW["dividend_report"][2]["payment_date"]
                }
            ],
            "monthly_report": []
        }
    }
}

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
