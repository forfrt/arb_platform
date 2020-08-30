from binance.client import Client

api_key = "W7xrWkVTfY0QdvpfwNhrkIOxSsqAzb2y6C1QchUvxleSDuglYABauqIuriLsxQYI"
api_secret = "ahljeb65Y5uxbyoQcexdZtdhcXdDBUUZHZAcww0GMbm9SmQ0L6WoVjf1xRV7vHjD"

client = Client(api_key, api_secret, {"verify":False,"timeout": 20})

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('BNBBTC', process_message)
bm.start()

# get historical kline data from any date range

# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

# fetch weekly klines since it listed
klines = client.get_historical_klines("NEOBTC", KLINE_INTERVAL_1WEEK, "1 Jan, 2017")
