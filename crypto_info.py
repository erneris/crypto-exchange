from requests import get

def get_currencies():
    currencies = []
    request = get("https://api.coincap.io/v2/assets").json()["data"]
    for currency in request:
        currencies.append({"id": currency["rank"], "symbol": currency["symbol"], "name": currency["name"], "price": round(float(currency["priceUsd"]), 2)})
    return currencies

def get_data(symbol):
    currencies = get_currencies()
    for currency in currencies:
        if currency["symbol"].lower() == symbol.lower():
            return currency
    return False