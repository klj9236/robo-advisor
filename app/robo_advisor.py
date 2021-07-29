# this is the "app/robo_advisor.py" file
#conda create -n stocks-env python=3.8 # (first time only)
#conda activate stocks-env

#pip install -r requirements.txt

import requests #still need to import even tho its installed. Just do this once


request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

from pandas import read_csv
stats_df = read_csv(request_url) 
print(type(stats_df))
print(stats_df.head())

quit() #stops the rest of the program from running


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
