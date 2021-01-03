import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from commonFunctionFile import *


def PRINT(label):
	for x in range(len(label)):
		print(label[x])
def getData(symbol):
	try:
		print(symbol)
		tickerSymbol = symbol
		tickerData = yf.Ticker(tickerSymbol)
		tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2020-1-1')
		if(tickerDf.empty):
			return 0
		else:
			return 1
	except:
		return 0


def getInfo():
	tickerSymbol = 'MSFT'
	tickerData = yf.Ticker(tickerSymbol)
	PRINT(tickerData.info)
	# get upcoming event
	PRINT(tickerData.calendar)
	#get recommendation data for ticker
	PRINT(tickerData.recommendations)
def get():
	tsla_df = yf.download('TSLA', 
                      start='2019-01-01', 
                      end='2019-12-31', 
                      progress=False)
	PRINT(tsla_df.head())

def getNPlot():
	ticker = yf.Ticker('TSLA')
	tsla_df = ticker.history(period="max")
	tsla_df['Close'].plot(title="TSLA's stock price")

TICKER_FILE='samplelist.csv'
TICKER_FILE='allIndianTicker.csv'

symbols = f_TICKER(TICKER_FILE)
a_dict={}
for i in range(len(symbols)):
	if(getData(symbols.SYMBOL[i])):
		a_dict[symbols.SYMBOL[i]] = 1
	else:
		a_dict[symbols.SYMBOL[i]] = 0


a_file = open("stockeaderesult.csv", "w")
writer = csv.writer(a_file)
for key, value in a_dict.items():
    writer.writerow([key, value])
a_file.close()


