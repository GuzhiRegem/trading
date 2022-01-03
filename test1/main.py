# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

data = yf.download(tickers='UBER', period='5m', interval='5m')
#Print data
print(data)