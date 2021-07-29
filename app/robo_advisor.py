# this is the "app/robo_advisor.py" file
#conda create -n stocks-env python=3.8 # (first time only)
#conda activate stocks-env

#pip install -r requirements.txt

import requests #still need to import even tho its installed. Just do this once


request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

from pandas import read_csv
price_df = read_csv(request_url) 


latest_day = (price_df.iloc[0,0])

#request_at = (price_df.iloc[0])
def to_usd(my_price):
    return f"${my_price:,.2f}"

recent_low = price_df["low"].min()
recent_high = price_df["high"].max()
latest_close = price_df.iloc[0,4]

import pandas as pd

df = pd.DataFrame(price_df, columns=["timestamp", "open", "high", "low", "close", "volume"])

df.to_csv("data/prices.csv", index=False)

quit()

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
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


