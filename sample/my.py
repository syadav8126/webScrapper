from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError

try:
	html = urlopen("https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI")
except HTTPError as e:
	print(e)
except URLError:
	print("Server down or incorrect domain")
else:
	res = bs(html.read(), "html5lib")
	# filter a tag by the help of class name
	#tags = res.findAll("h2", {"class": "widget-title"})

	# filter span tag with 
	#tags = res.findAll("div", {"class": "pnc_wrapper"})
	tags = res.findAll("div", {"id": "standalone"})
	#ret elemennts matching the text
	#tags = res.findAll(text="Python Programming Basics with Examples")
	# get children elements 
	#tags = res.span.findAll("li")

	print(tags)

<li class="li_all li-S-income-3 active"><a aria-expanded="true" data-toggle="tab" href="#S-income-3" onclick="getFinancialTabData('income','S','S-income_statement','3')">Quarterly</a></li>

