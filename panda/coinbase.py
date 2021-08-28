import requests
import pandas as pd
import time
from datetime import datetime, timedelta

apiUrl = "https://api.pro.coinbase.com"
sym = "BTC-USD"
timeFrame = 15
barSize = timeFrame*60

timeEnd = datetime.now()
delta = timedelta(minutes = timeFrame)
timeStart = timeEnd - (300*delta)

timeStart = timeStart.isoformat()
timeEnd = timeEnd.isoformat()

parameters = {
	"start": timeStart,
	"end": timeEnd,
	"granularity": barSize,
}
data = requests.get(f"{apiUrl}/products/{sym}/candles",
	params = parameters,
	headers = {"content=type":"application/json"})

df = pd.DataFrame(data.json(),
		columns = ["time", "low", "high", "open", "close", "volume"])

df["date"] = pd.to_datetime(df["time"], unit='s')
df = df[["date", "open", "high", "low", "close"]]
df.set_index("date", inplace = True)

df = df.resample("240 min").agg({
	"open":"first",
	"high":"max",
	"low":"min",
	"close":"last"
	})

df.reset_index(inplace = True)
df = df.dropna()

print(df)
