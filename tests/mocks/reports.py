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
