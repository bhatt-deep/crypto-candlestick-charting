# fetch ohlc data from binance for ADAUSDT and plot it on a candlestick chart.
import pandas as pd
import mplfinance as mpf
import requests

# fetch data from binance
url = 'https://api.binance.com/api/v3/klines?symbol=ADAUSDT&interval=1m&limit=500'
data = requests.get(url).json()
df = pd.DataFrame(data)
df.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
df = df[['open_time', 'open', 'high', 'low', 'close', 'volume']]
df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
df.set_index('open_time', inplace=True)
df = df.astype(float)

# plot data
mpf.plot(df, type='candle', style='yahoo', volume=True, title='ADAUSDT', ylabel='Price', ylabel_lower='Volume')
