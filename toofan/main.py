from commonFunctionFile import *
from nsepy.symbols import *
from getlinks import *

data=pd.DataFrame()
a_dict={}
TICKER_FILE='allIndianTicker.csv'
start = datetime.datetime(2020,12,30)
end   = datetime.datetime(2020,12,31)

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

symbol='ACC'
#this = single_symbol(symbol)
pd = links()
for p in pd:
	lok = p.find(symbol.lower())
	if (lok>0):
		print("got",symbol,"in",p,"at location",lok)
#print(pd.loc[lok,:])
