# this is the "app/robo_advisor.py" file
#conda create -n stocks-env python=3.8 # (first time only)
#conda activate stocks-env

#pip install -r requirements.txt

import requests #still need to import even tho its installed. Just do this once
from dotenv import load_dotenv
import os

symbol = input("PLEASE ENTER STOCK SYMBOL: ")
print(symbol)

#validation symbol
if (len(symbol)>=1<=5):
    print("VALID SYMBOL")


api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&datatype=csv"

from pandas import read_csv
price_df = read_csv(request_url) 


latest_day = (price_df.iloc[0,0])

#request_at = (price_df.iloc[0])
def to_usd(my_price):
    return f"${my_price:,.2f}"

recent_low = price_df["low"].min()
recent_high = price_df["high"].max()
latest_close = price_df.iloc[0,4]



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
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


