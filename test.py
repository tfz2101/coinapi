from coinapi_v1 import CoinAPIv1
import datetime
import pandas as pd
import numpy as np

test_key = '7C973F6B-9E95-49DA-8E9E-55F35FC3092F'

api = CoinAPIv1(test_key)
exchanges = api.metadata_list_exchanges()
start = datetime.datetime(2018, 7, 28, 6, 19, 51, 0).isoformat()
end = datetime.datetime(2018, 7, 30, 0, 0, 0, 0).isoformat()

historical_trades_eth = api.trades_historical_data('COINBASE_SPOT_ETH_USD', {'time_start': start, 'time_end': end, 'limit': 10000})

historical_trades_eth = pd.DataFrame(historical_trades_eth)

writer = pd.ExcelWriter('eth_dataset_07_28_2018_1.xlsx')
historical_trades_eth.to_excel(writer, 'set1')
writer.save()

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