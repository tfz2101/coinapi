import numpy as np
import pandas as pd
import datetime
import time
import sys
sys.path.append('../')
from ML_Trading import Signals_Testing as st
from pytz import timezone
import requests
import urllib.request
import json

API_FILE = '../nomics.txt'
with open(API_FILE) as f:
    lines = [line.rstrip('\n') for line in open(API_FILE)]
print(lines)

KEY = str(lines[0])

#See available exchanges and currencies
url = "https://api.nomics.com/v1/markets?key=" + KEY
result = json.loads(urllib.request.urlopen(url).read())
for element in result:
    print(element)

'''
#Exchange OHLCV
EXCHANGE = 'gdax'
FREQ = '1m'
url = "https://api.nomics.com/v1/exchange_candles?key=" + KEY + '&interval=' + FREQ + '&exchange='
                                                        binance&market=BTCUSDT&start=2018-04-14T00%3A00%3A00Z&end=2018-05-14T00%3A00%3A00Z"
print(urllib.request.urlopen(url).read())
'''

'''
start_date = datetime.datetime(2018, 7, 26, 0, 0, 0)
start_date = time.mktime(start_date.timetuple())
print('start date',start_date)
url = "https://api.bitfinex.com/v1/lends/eth/?limit_lends=4000?timestamp=" + str(start_date)

response = requests.request("GET", url)

data = response.json()
transactions = []
for trade in data:

    rate = trade['rate']
    amount_lent = trade['amount_lent']
    amount_used = trade['amount_used']
    ts = int(trade['timestamp'])
    time = datetime.datetime.fromtimestamp(ts)
    print('time', time)
    transactions.append([time, rate, amount_lent, amount_used])

transactions_pd = pd.DataFrame(transactions, columns=['time', 'rate', 'amount_lent', 'amount_used'])

print(transactions_pd)
st.write(transactions_pd, 'eth_lending_rates.xlsx','sheet1')
'''