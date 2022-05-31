import datetime as dt

import pandas_datareader.data as web

from arch import arch_model

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 3, 8)
sp500 = web.DataReader('FTR', 'yahoo', start=start, end=end)
returns = 100 * sp500['Adj Close'].pct_change().dropna()
am = arch_model(returns)
res = am.fit()
fig = res.plot(annualize='D')
print(res.summary())
