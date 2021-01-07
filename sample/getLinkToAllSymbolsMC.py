from urllib.request import urlopen
import re
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError

try:
	html = urlopen("https://www.moneycontrol.com/india/stockpricequote/Z")
except HTTPError as e:
	print(e)
except URLError:
	print("Server down or incorrect domain")
else:
	# filter a tag by the help of class name
	#tags = res.findAll("h2", {"class": "widget-title"})

	# filter span tag with 
	#tags = res.findAll("span", {"title": "Stocks"})
	#tags = res.findAll("tr", {"bgcolor": "#f6f6f6"})
	#ret elemennts matching the text
	#tags = res.findAll(text="Python Programming Basics with Examples")
	# get children elements 
	#tags = res.span.findAll("tbody")
	#tag = res.findAll("div", {"class":"PT15"})
	#tags = tag.find("tr", {"bgcolor":"#f6f6f6"})
	#tags = tag.findAll('a', attrs={'href':re.compile("^https://")})
	#print(tags)
	res = bs(html.read(), "html5lib")
	tag = res.find("div", {"class":"PT15"})
	for link in tag.findAll('a', attrs={'href':re.compile("^http://")}):
		print(link.get('href'))
	#print(tags)

def alllink():
	res = bs(html.read(), "html5lib")
	tag = res.find("div", {"class":"PT15"})
	for link in tag.findAll('a', attrs={'href':re.compile("^https://")}):
		print(link.get('href'))
	
