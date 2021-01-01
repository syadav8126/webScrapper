import requests
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd
import re

#s='\<span class\=\"line\-through\" data\-price\=\"(.*)\ USD'
s='\d+\.\d+'

url_1 = 'https://www.zara.com/us/en/woman-dresses-l1066.html?v1=1180427'
zara_page = requests.get(url_1)
zara_soup = BeautifulSoup(zara_page.content, 'lxml')
names = zara_soup.findAll('a',{'class','name'})
product_names = [item.text for item in names]
prices = zara_soup.findAll('div',{'class','_product-price'})
prod_prices = [float(re.search(s,str(item)).group(0)) for item in prices]

for x in range(len(prices)):
	print(product_names[x], ":", prod_prices[x])
	# .text should get all the test in the line but since in this case the line will be surrounded with span, will ret nothing.
	#print(prices[x].text)
