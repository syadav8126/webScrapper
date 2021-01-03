import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('ggplot')
#%matplotlib inline

start = datetime.datetime(2012,1,1)
end = datetime.datetime(2020,12,12)
google=web.DataReader("TSLA", 'yahoo', start, end)

def AVERAGE(data):
	#data = pd.read_csv('AAPL.csv', index_col=0)
	data.index = pd.to_datetime(data.index, dayfirst=True)

	data['12d_EMA'] = data.Close.ewm(span=12, adjust=False).mean()
	data['26d_EMA'] = data.Close.ewm(span=26, adjust=False).mean()
	data[['Close','12d_EMA','26d_EMA']].plot(figsize=(10,5))
	plt.legend()
	#plt.show()

	# Calculate MACD
	data['macd'] = data['12d_EMA']- data['26d_EMA'] 
	# Calculate Signal
	data['macdsignal'] = data.macd.ewm(span=9, adjust=False).mean()
	data[['macd','macdsignal']].plot(figsize=(10,5))
	##plt.show()
#macd and macdsignal combines and create Trading signal that will tell when to  buy or purchase the stock, 
def TRADINGSIGNAL(data):
	# Define Signal
	data['trading_signal'] = np.where(data['macd'] > data['macdsignal'], 1, -1)
	# Calculate Returns
	data['returns'] = data.Close.pct_change()
	# Calculate Strategy Returns
	data['strategy_returns'] = data.returns * data.trading_signal.shift(1)
	# Calculate Cumulative Returns
	global cumulative_strategy_returns
	cumulative_strategy_returns = (data.strategy_returns + 1).cumprod()
	# Plot Strategy Returns
	cumulative_strategy_returns.plot(figsize=(10,5))
	plt.legend()
	##plt.show()
# Compound Annual Growth Rate
def CAGR(data):
	print("CAGR")
	# Total number of trading days
	days = len(cumulative_strategy_returns)
	# Calculate compounded annual growth rate
	# 252 = total trading days in a year
	annual_returns = (cumulative_strategy_returns.iloc[-1]**(252/days) - 1)*100
	print('The CAGR is %.2f%%' % annual_returns)

	# Calculate the annualised volatility
	# the variation in stcok priice over a time period
	annual_volatility = data.strategy_returns.std() * np.sqrt(252) * 100
	print('The annualised volatility is %.2f%%' % annual_volatility)

	# Sharpe ratio : the risk taken in comparision to risk free investments(FD/RD/Bank Savings)
	# Assume the annual risk-free rate is 4%, as bank return principal at 4% interest
	# 252 = total trading days in a year
	risk_free_rate = 0.04
	daily_risk_free_return = risk_free_rate/252

	# Calculate the excess returns by subtracting the daily returns by daily risk-free return
	excess_daily_returns = data.strategy_returns - daily_risk_free_return

	# Calculate the sharpe ratio using the given formula
	sharpe_ratio = (excess_daily_returns.mean() /
        	        excess_daily_returns.std()) * np.sqrt(252)

	print('The Sharpe ratio is %.2f' % sharpe_ratio)


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
	# total return on Day T from Day 1
	google['CUM'] = (1 + google['returns']).cumprod()
	google['CUM'] = google['CUM'] * 10
	google['CUM'].plot(label = 'return')
	plt.legend()
	plt.show()
	
AVERAGE(google)
TRADINGSIGNAL(google)
CAGR(google)
