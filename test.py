from coinapi_v1 import CoinAPIv1
import datetime
import pandas as pd

test_key = '7C973F6B-9E95-49DA-8E9E-55F35FC3092F'

api = CoinAPIv1(test_key)
exchanges = api.metadata_list_exchanges()
start = datetime.date(2018, 7, 5).isoformat()
end = datetime.date(2018, 7, 7).isoformat()

historical_trades_btc = api.trades_historical_data('COINBASE_SPOT_BTC_USD', {'time_start': start, 'time_end': end, 'limit': 10000})

historical_trades_btc = pd.DataFrame(historical_trades_btc)

writer = pd.ExcelWriter('dataset_07_05_2018.xlsx')
historical_trades_btc.to_excel(writer, 'set1')
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