import yfinance as yf
import pandas as pd
import mplfinance as mpf

df = yf.Ticker("BTC-USD").history(period="max")
df = df.loc["2021-01-01":]
df["50ma"] = (df["Open"].rolling(window=50).mean())/1.5

apds = [mpf.make_addplot(df["50ma"])]
mpf.plot(df, type="candle", volume = False, mav = (13,21), addplot =apds)