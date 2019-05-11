from typing import Dict
import json
import pprint

import requests

def get_stock_prices():
    url: str = "https://www.alphavantage.co/query"
    params: Dict[str, str] = {
        "function" : "TIME_SERIES_DAILY_ADJUSTED",
        "symbol" : "CBA.AX",
        "apikey" : "redacted"
    }
    resp: requests.Response = requests.get(url, params=params)
    data = json.loads(resp.text)
    return data
