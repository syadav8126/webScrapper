from finology import spiderController
import pandas as pd

SYMBOL='COALINDIA'
SYMBOL='HINDUNILVR'
global mode
global DATA

mode='C'

def getIndex(df, token):
	pos = list()
	res = df.isin([token])
	series = res.any()
	col = list(series[series==True].index)
	for c in col:
		row = list(res[c][res[c]==True].index)
		for r in row:
			pos.append((r,c))
	assert(pos)
	return pos
def getNetProfit(pnl, year):
	if (mode=='C'):
		pos = getIndex(pnl, "Consolidated Net Profit")
	else:
		pos = getIndex(pnl, "Net Profit")
	return pnl._get_value(pos[0][0], year)
def getOpProfit(pnl, year):
	pos = getIndex(pnl, "Operating Profit")
	return pnl._get_value(pos[0][0], year)
def getShareCap(bs, year):	
	pos = getIndex(bs, "Share Capital")
	return bs._get_value(pos[0][0], year)
def getTotalReserves(bs, year):
	pos = getIndex(bs, "Total Reserves")
	return bs._get_value(pos[0][0], year)
def getBorrowings(bs, year):
	pos = getIndex(bs, "Borrowings")
	return bs._get_value(pos[0][0], year)

def roce(bs, pnl):
	'''
		total equity = Share Capital  + Total Reserves
		roce  operating profit / (total equity + Borrowings)
	'''
	columnsNamesArr = bs.columns.values
	latest_year 	= columnsNamesArr[-1]
	share_cap 	= getShareCap(bs, latest_year)
	tot_res 	= getTotalReserves(bs, latest_year)
	borrowing 	= getBorrowings(bs, latest_year)
	operating_profit = getOpProfit(pnl, latest_year)
	print(latest_year, share_cap, tot_res, borrowing, operating_profit)
	return operating_profit/(share_cap+tot_res+borrowing)

def roe(bs, pnl):
	'''
		total equity = Share Capital  + Total Reserves
		roe = Net Profit(profit after tax)/(total equity)
	'''
	columnsNamesArr = bs.columns.values
	latest_year = columnsNamesArr[-1]
	net_pr = getNetProfit(pnl, latest_year)
	share_cap = getShareCap(bs, latest_year)
	tot_res = getTotalReserves(bs, latest_year)
	print(latest_year, share_cap, tot_res, net_pr)
	return net_pr/(share_cap+tot_res)
		
def getdataFinology(symbol):
	DATA=spiderController(symbol, mode=mode)
	quaterly = pd.DataFrame(DATA[1])
	pnl = pd.DataFrame(DATA[2])
	balance_sheet = pd.DataFrame(DATA[3])
	cash_flow = pd.DataFrame(DATA[4])

	print(roce(balance_sheet, pnl))
	print(roe(balance_sheet, pnl))


getdataFinology(SYMBOL)
