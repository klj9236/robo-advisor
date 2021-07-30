# this is the "app/robo_advisor.py" file
#conda create -n stocks-env python=3.8 # (first time only)
#conda activate stocks-env

#pip install -r requirements.txt

import requests #still need to import even tho its installed. Just do this once
from dotenv import load_dotenv
import os

symbol = input("PLEASE ENTER STOCK SYMBOL: ")
print(symbol)

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&datatype=csv"

from pandas import read_csv
price_df = read_csv(request_url) 

#validation symbol
#if symbol not in price_df:
#    print("SORRY SYMBOL NOT FOUND")

if (len(symbol)>=1<=5 and symbol.isalpha()):
    print("VALID SYMBOL")

else: 
    print("INVALID SYMBOL")
    quit()

latest_day = (price_df.iloc[0,0])

#request_at = (price_df.iloc[0])
def to_usd(my_price):
    return f"${my_price:,.2f}"

recent_low = price_df["low"].min()
recent_high = price_df["high"].max()
latest_close = price_df.iloc[0,4]
average_price = price_df["close"].mean()



#below code from https://www.programiz.com/python-programming/datetime/timestamp-datetime
from datetime import datetime
# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
dt_object = datetime.fromtimestamp(timestamp)


import pandas as pd

df = pd.DataFrame(price_df, columns=["timestamp", "open", "high", "low", "close", "volume"])

df.to_csv("data/prices.csv", index=False)





print("-------------------------")
print(f"SELECTED SYMBOL: {(symbol.upper())}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST MADE AT: {(dt_object)}")
print("-------------------------")
print(f"LATEST DAY: {(latest_day)}")
print(f"LATEST CLOSE: {to_usd(latest_close)}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print(f"AVERAGE PRICE: {to_usd(float(average_price))}")
print("-------------------------")
if float(average_price)>float(latest_close):
    print("RECOMMENDATION: BUY!")
elif float(average_price)<float(latest_close):
    print("RECOMMENDATION: SELL!")
print("RECOMMENDATION REASON: IF LATEST CLOSE IS ABOVE 100 DAY AVERAGE, SELL! IF LATEST CLOSE IS BELOW 100 DAY AVERAGE, BUY!")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


