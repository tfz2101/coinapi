from coinapi_v1 import CoinAPIv1
import datetime
import pandas as pd
import numpy as np
import json
import requests
import sys
sys.path.append('../')
from ML_Trading import ML_functions as mlfcn
from ML_Trading import Signals_Testing as st
from ML_Trading import Stat_Fcns as sf


def write(datadf, path, tab="Sheet1"):
    WRITE_PATH = path
    writer = pd.ExcelWriter(WRITE_PATH, engine='xlsxwriter')
    datadf.to_excel(writer, sheet_name=tab)
    writer.save()


free_key = '7C973F6B-9E95-49DA-8E9E-55F35FC3092F'
startup_key = 'F717F31A-3C05-4D9A-A824-69FEF27CBC57'


api = CoinAPIv1(free_key)
exchanges = api.metadata_list_exchanges()
start = datetime.datetime(2018, 6, 28, 14, 0, 0, 0).isoformat()
end = datetime.datetime(2018, 6, 30, 0, 0, 0, 0).isoformat()
symbol = 'BITMEX_SPOT_BTC_USD' #BITMEX_PERP_BTC_USD
interval = '30MIN'
file_name = 'bitmex_BTC_dataset_'


#GET OHLCV DATA FOR MULTIPLE PULLS

'''for index in range(0,1):
    ohlcv_historical = api.ohlcv_historical_data(symbol,{'period_id': interval, 'time_start': start, 'time_end': end})
    
    historical_trades_eth = pd.DataFrame(historical_trades_eth)
    write(historical_trades_eth, file_name + ' ' + str(index) + '.xlsx', 'sheet1')

    data = historical_trades_eth

    last_date = str(data.ix[data.shape[0]-1,'time_exchange'])
    last_date = datetime.datetime.strptime(last_date, '%Y-%m-%dT%H:%M:%S.%f0000Z')
    last_date_round = datetime.datetime(last_date.year, last_date.month, last_date.day, last_date.hour, last_date.minute, last_date.second, 0)
    print('last date', last_date_round.isoformat())
    last_date_round = last_date_round.isoformat()


    start = last_date_round
'''

#GET OHLCV DATA
#ohlcv_historical = api.ohlcv_historical_data(symbol,{'period_id': interval, 'time_start': start, 'time_end': end, 'limit': 20000})
ohlcv_historical = api.trades_historical_data(symbol, {'time_start': start, 'time_end': end, 'limit': 10000})
ohlcv_historical = pd.DataFrame(ohlcv_historical)
print('data', ohlcv_historical)
st.write_new(ohlcv_historical, 'bitmex_BTC_Tick_6_30_2018_3.xlsx', 'raw_data')

timeindex = ohlcv_historical['time_exchange'].values

for i in range(0, timeindex.shape[0]):
    timeindex[i] = datetime.datetime.strptime(timeindex[i], '%Y-%m-%dT%H:%M:%S.%fZ')
    print('time index', timeindex[i])

clean_data = ohlcv_historical.loc(['price','size','side'])
clean_data = clean_data.set_index(timeindex)
st.write(clean_data, 'bitmex_BTC_Tick_6_30_2018.xlsx', 'clean_data' )




#LOOK AT THE LIST OF EXCHANGES AND SYMBOLS CODES
'''
api = CoinAPIv1(startup_key)
exchanges = api.metadata_list_exchanges()

symbols = api.metadata_list_symbols()
print('Symbols')
for symbol in symbols:
    try:
        print('Symbol ID: %s' % symbol['symbol_id'])
        print('Exchange ID: %s' % symbol['exchange_id'])
        print('Symbol type: %s' % symbol['symbol_type'])
        print('Asset ID quote: %s' % symbol['asset_id_quote'])
    except:
        pass

out = pd.DataFrame(symbols)
write(out, 'coinapi_symbols', 'sheet1')
'''

'''
#JOIN SHEETS INTO ONE BIG DATASET
data1 = pd.read_excel('eth_dataset_07_15_07_19_A.xlsx','set1')
data2 = pd.read_excel('eth_dataset_07_15_07_19_B.xlsx','set1')

data_total = data1.set_index('uuid').append(data2.set_index('uuid')).drop_duplicates()
print('data_total', data_total)
write(data_total, 'eth_dataset_07_15.xlsx', 'set1')
'''


'''
for data in historical_trades_btc:
    print('Symbol ID: %s' % data['symbol_id'])
    print('Time Exchange: %s' % data['time_exchange'])
    print('Time CoinAPI: %s' % data['time_coinapi'])
    print('UUID: %s' % data['uuid'])
    print('Price: %s' % data['price'])
    print('Size: %s' % data['size'])
    print('Taker Side: %s' % data['taker_side'])
'''

'''
orderbooks_historical_data_btc_usd = api.orderbooks_historical_data('BITSTAMP_SPOT_BTC_USD', {'time_start': start})


for data in orderbooks_historical_data_btc_usd:
    print('Symbol ID: %s' % data['symbol_id'])
    print('Time Exchange: %s' % data['time_exchange'])
    print('Time CoinAPI: %s' % data['time_coinapi'])
    print('Asks:')
    for ask in data['asks']:
        print('- Price: %s' % ask['price'])
        print('- Size: %s' % ask['size'])
    print('Bids:')
    for bid in data['bids']:
        print('- Price: %s' % bid['price'])
        print('- Size: %s' % bid['size'])
        
'''

#CANCEL SUSCRIPTION
'''
import requests
url = 'https://rest.coinapi.io/v1/subscription/cancel'
headers = {'X-CoinAPI-Key' : startup_key}
response = requests.get(url, headers=headers)
'''