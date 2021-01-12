from commonFunctionFile import *
from nsepy.symbols import *
from links import *
import csv
from financial import *

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

def linkToSymbolTickerFile():
	pass
def nameOfCompany(fl):
	names = pd.read_csv(fl)
	names = names['NAME OF COMPANY']
	for name in names:
		print(":",name)
def getSymbol(TICKER_FILE):
	sym_name = f_TICKER(TICKER_FILE)
	sym = sym_name['SYMBOL']
	name = sym_name['NAME OF COMPANY']
	for s in range(len(sym)):
		print(sym[s])
		print(name[s])
def search():
	sym_n = f_TICKER(TICKER_FILE)
	sym  = sym_n['SYMBOL']
	name = sym_n['NAME OF COMPANY']
	#sym=["ABAN","ABAN"]
	#name=["Aban Offshore Limited","Aban Offshore Limited"]
	for s in range(len(sym)):
		nameSecondWord = name[s].split()[1]
		nameSecondWord = nameSecondWord.lower()
		#print("nameSecondWord",nameSecondWord)
		with open("symbollink.csv") as o:
			for line in o:
				if sym[s] in line:
					if nameSecondWord in line:
						with open('precisesymbollink.csv','a', encoding='utf-8') as fl:
							print(sym[s],nameSecondWord,line)
							fl.write(str(line))

def callCrappy():
	process.crawl(MySpider,time_frame='frequency=3')
	process.start()
