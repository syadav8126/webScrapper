from urllib.request import urlopen
import re
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError

def links():
	try:
		html = urlopen("https://www.moneycontrol.com/india/stockpricequote/A")
	except HTTPError as e:
		print(e)
	except URLError:
		print("Server down or incorrect domain")
	else:
		lyst = []
		res = bs(html.read(), "html5lib")
		tag = res.find("div", {"class":"PT15"})
		for link in tag.findAll('a', attrs={'href':re.compile("^http://")}):
			lynk=str(link.get('href'))
			lyst += [lynk]
			
		return lyst

