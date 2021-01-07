from commonFunctionFile import *
from nsepy.symbols import *

data=pd.DataFrame()
a_dict={}
TICKER_FILE='allIndianTicker.csv'
start = datetime.datetime(1970,12,31)
end   = datetime.datetime(2020,12,31)

def multi_symbol(TICKER_FILE):
	ticker = f_TICKER(TICKER_FILE)
	for i in range(len(ticker)):
		frame = f_DATA(ticker.SYMBOL[i],start, end)
		name = ticker.SYMBOL[i]
		if(frame.empty):
			print(ticker.SYMBOL[i],"=0")
			a_dict[ticker.SYMBOL[i]] = 0
		else:
			print(ticker.SYMBOL[i],"=1")
			a_dict[ticker.SYMBOL[i]] = 1

def single_symbol(symbol):
	frame = f_DATA(symbol, start, end)
	if(frame.empty):
		print(symbol,"= 0")
	else:
		print(symbol,"= 1")
	return frame
	
def f_WRITEtoFILE(saveinFile, a_dict):
	a_file = open(saveinFile, "w")
	writer = csv.writer(a_file)
	for key, value in a_dict.items():
		writer.writerow([key, value])
	a_file.close()

symbol='SBIN'
this = single_symbol(symbol)
CUMULATIVE_RETURN(this)
