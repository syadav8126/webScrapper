from urllib.request import urlopen
import re
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError
from csv import writer

def links(seq):
	try:
		url = 'https://www.moneycontrol.com/india/stockpricequote/'
		com = seq[0].upper()
		com="others"
		com_url = url+com
		html = urlopen(com_url)
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
		with open('filelink.txt', 'a') as f:
			for item in lyst:
				f.write("%s\n" % item)
			
		return lyst

