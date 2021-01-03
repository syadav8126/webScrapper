import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
import requests
import re
import json

# Enter a stock symbol
index= 'MSFT'

url_is = 'https://finance.yahoo.com/quote/' + index + '/financials?p=' + index
url_bs = 'https://finance.yahoo.com/quote/' + index +'/balance-sheet?p=' + index
url_cf = 'https://finance.yahoo.com/quote/' + index + '/cash-flow?p='+ index
read_data = ur.urlopen(url_is).read() 
soup_is= BeautifulSoup(read_data,'lxml')

ls= [] # Create empty list
for l in soup_is.find_all('div'): 
  #Find all data structure that is ‘div’
  ls.append(l.string) # add each element one by one to the list
 
ls = [e for e in ls if e not in ('Operating Expenses','Non-recurring Events')] # Exclude those columns
new_ls = list(filter(None,ls))
print(new_ls)
new_ls = new_ls[12:]
#is_data = list(zip(*[iter(new_ls)]*7))
print("  ------------------------")
df = pd.DataFrame(new_ls)
print(df)
'''
df = df.set_index(0)
df = df.transpose()
print(df)
#for i in range(len(new_ls)):
#	print(new_ls[i])

Income_st = pd.DataFrame(df[0:])
print(Income_st)
'''
