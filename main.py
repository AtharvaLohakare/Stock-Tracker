import requests

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

url = "https://www.alphavantage.co/query"

def stock_data(quote):
    symbol = quote["01. symbol"]
    open = quote["02. open"]
    high = quote["03. high"]
    low = quote["04. low"]
    price = quote["05. price"]
    volume = quote["06. volume"]
    latest_trading = quote["07. latest trading day"]
    prev_close = quote["08. previous close"]
    change = quote["09. change"]
    change_percent = quote["10. change percent"]

    print("=" * 30)
    print("      STOCK PRICE TRACKER")
    print("=" * 30)
    print("Symbol            :", symbol)
    print("Open              :", open)
    print("High              :", high)
    print("Low               :", low)
    print("Price             :", price)
    print("Volume            :", volume)
    print("Latest Trading Day:", latest_trading)
    print("Previous Close    :", prev_close)
    print("Change            :", change)
    print("Change %          :", change_percent)
    print("=" * 30)

while True:
    stock = input("Enter Stock Name :")
    if stock == "exit":
        break
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": stock,
        "apikey": api_key
    }

    response = requests.get(url, params=params)

    data = response.json()
    print(data)
    if "Global Quote" not in data:
        print("Unable to get stock data.")
    else:
        quote = data["Global Quote"]

        print("Invalid Stock")
        stock_data(quote)