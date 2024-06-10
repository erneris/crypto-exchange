import requests
from sys import exit

def get_currencies():
    currencies = []
    try:
        request = requests.get("https://api.coincap.io/v2/assets").json()["data"]
    except requests.JSONDecodeError:
        print("An error has accured while getting cryptocurrency data, please try again later")
        exit()

    for currency in request:
        if float(currency["priceUsd"]) < 0.01:
            currency["priceUsd"] = 0.01
        currencies.append({"id": currency["rank"], "symbol": currency["symbol"], "name": currency["name"], "price": round(float(currency["priceUsd"]), 2)})
    return currencies

def get_data(symbol):
    currencies = get_currencies()
    for currency in currencies:
        if currency["symbol"].lower() == symbol.lower():
            return currency
    return False