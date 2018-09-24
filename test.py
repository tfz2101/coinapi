from coinapi_v1 import CoinAPIv1
import datetime
import pandas as pd
import numpy as np



def write(datadf, path, tab="Sheet1"):
    WRITE_PATH = path
    writer = pd.ExcelWriter(WRITE_PATH, engine='xlsxwriter')
    datadf.to_excel(writer, sheet_name=tab)
    writer.save()


free_key = '7C973F6B-9E95-49DA-8E9E-55F35FC3092F'
startup_key = 'F717F31A-3C05-4D9A-A824-69FEF27CBC57'


api = CoinAPIv1(startup_key)
exchanges = api.metadata_list_exchanges()
start = datetime.datetime(2018, 9, 4, 0, 0, 0, 0).isoformat()
end = datetime.datetime(2018, 9, 8, 0, 0, 0, 0).isoformat()
file_name = 'eth_dataset_09_04_09_08'

for index in range(0,4):
    historical_trades_eth = api.trades_historical_data('COINBASE_SPOT_ETH_USD', {'time_start': start, 'time_end': end, 'limit': 20000})
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