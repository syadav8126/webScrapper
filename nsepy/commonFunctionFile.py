import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import csv
from nsepy import get_history
from datetime import date

start = datetime.datetime(2020,12,30)
end   = datetime.datetime(2020,12,31)

def f_DATA(ticker, start, end):
	
	try:
		data = get_history(ticker, start, end)
	except:
		data= pd.DataFrame()

	print(type(data))
	return data


def PLOT(google):
	google['Open'].plot(label = 'open price')
	google['Close'].plot(label = 'Close price')
	google['High'].plot(label = 'High price')
	google['Low'].plot(label = 'Low price')
	plt.legend()
	plt.title('STOCK PRICES')
	plt.ylabel('Stoce prices')
	plt.show()

def SAVECSV(google):
	print(type(google))
	return
	google.to_csv('/home/toofan/webScrapper/sample.csv')

def MISC(google):
	# Cal maximux
	print(google['Volume'].argmax())
	# Location where Volume is Max
	print(google.iloc[google['Volume'].argmax()])
def MAVG(google):
	# cal Moving average over 50 count on Open price
	google['MA50'] = google['Open'].rolling(50).mean()
	google['Open'].plot(label='Open')
	google['MA50'].plot(label='MA50')
	plt.show()
def RET(google):
	# returns = (closePrice@T)/(closePrice@(T-1)) - 1
	google['returns'] = (google['Close']/google['Close'].shift(1)) - 1
	print(google['returns'])
	# draw Histogram
	google['returns'].hist(bins=50)

def CUMULATIVE_RETURN(google):
	RET(google)
	# total return on Day T from Day 1
	google['CUM'] = (1 + google['returns']).cumprod()
	google['CUM'] = google['CUM'] * 10
	google['CUM'].plot(label = 'return')
	plt.legend()
	plt.show()
	
def f_TICKER(LIST_FILE):
	return pd.read_csv(LIST_FILE)
