import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials


def PRINT(label):
	for x in range(len(label)):
		print(label[x])
def getData(symbol):
	print(symbol)
	tickerSymbol = symbol
	tickerData = yf.Ticker(tickerSymbol)
	tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2020-1-1')
	print(tickerDf)

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

getData()

