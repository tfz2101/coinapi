from coinapi_v1 import CoinAPIv1
import datetime

test_key = '7C973F6B-9E95-49DA-8E9E-55F35FC3092F'

api = CoinAPIv1(test_key)
exchanges = api.metadata_list_exchanges()
start = datetime.date(2018, 7, 13).isoformat()
end = datetime.date(2018, 7, 15).isoformat()

historical_trades_btc = api.trades_historical_data('COINBASE_SPOT_BTC_USD', {'time_start': start, 'time_end': end})
print('len', len(historical_trades_btc))
#print('exchanges', exchanges)

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