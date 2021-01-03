from allFunction import *
import csv

data=pd.DataFrame()
a_dict={}
TICKER_FILE='listTicker.csv'
start = datetime.datetime(2020,12,31)
end   = datetime.datetime(2020,12,31)

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

a_file = open("result.csv", "w")
writer = csv.writer(a_file)
for key, value in a_dict.items():
    writer.writerow([key, value])
a_file.close()

