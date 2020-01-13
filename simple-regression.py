import pandas as panda
import quandl

# quandl API key
quandl.ApiConfig.api_key = "ecbo2idYx1Xsu_kFE5Wz"

df = quandl.get("WIKI/GOOGL")

#data shaping
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['High-Low Percent'] = ((df['Adj. High'] - df['Adj. Low'])/df['Adj. Close'] * 100)
df['Percent Change'] = ((df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'])

df = df[['Adj. Close', 'High-Low Percent', 'Percent Change', 'Adj. Volume']]
print(df.head())