import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data
sp = pd.read_csv('S&P500-Symbols.csv', index_col=[0])
