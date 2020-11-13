# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
import requests

style.use("ggplot")
start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)
df = web.DataReader("TSLA", "yahoo", start, end)
print(sys.version)
print(sys.executable)
r = requests.get("http://www.apple.com")
print(r.status_code)
# print(df.head())
df.plot()
plt.show()
