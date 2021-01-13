# -*- coding: utf-8 -*-
import scrapy
import sys
import csv
import json
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import Crawler
from pandas import DataFrame
import io
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
from sort import sort

OUTPUT=[]
class MySpider(scrapy.Spider):
	name = 'ntschools'
	start_urls = ['https://ticker.finology.in/company/COALINDIA']

	headers = {
		"accept": "application/json, text/javascript, */*; q=0.01",
		"accept-encoding": "gzip, deflate, br",
		"cookie": "ASP.NET_SessionId=m11vkz5l0t3wx4apdhjh4v4b; _ga=GA1.2.1056050435.1610270634; _gid=GA1.2.733890492.1610270634; _gat_gtag_UA_136614031_6=1; _fbp=fb.1.1610270633963.365948770",
		"referer": "https://ticker.finology.in/company/COALINDIA",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"accept-language": "en-US,en;q=0.9",
		"dnt": "1",
		"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		"x-requested-with": "XMLHttpRequest"
	}

	def __init__(self, *args, **kwargs):

		super(MySpider, self).__init__(*args, **kwargs)
		self.code    = kwargs.get('code')
			
	def parse(self, response, *args, **kwargs):

		#url = 'https://ticker.finology.in/GetPrices.ashx?v=3.1&fincode=219300&stk=BSE&type=Y&count=1'
		#url = 'https://ticker.finology.in/GetValuation.ashx?v=3.1&fincode=219300&exc=BSE&top=365'
		base_url = 'https://ticker.finology.in/Peers.ashx?v=3.1&fincode='
		code= str(self.code)
		url = base_url + code + '&Mode=S'
		print("====================================================================")
		print(url)
		#url = 'https://ticker.finology.in/GetShares.ashx?v=3.1&fincode=219300'
		#url = 'https://ticker.finology.in/GetCorpAction.ashx?v=3.1&fincode=219300'
		#url = 'https://ticker.finology.in/News.ashx?v=3.1&fincode=219300'
		#url = 'https://ticker.finology.in/GetCompanybrief.ashx?v=3.1&fincode=219300'
		request = scrapy.Request(url, callback=self.parse_api, headers=self.headers)
		yield request

	def parse_api(self, response):
		raw_data = response.body
		if not raw_data:
			return
		print(raw_data)
		data = raw_data.decode('UTF-8')
		ls = json.loads(data)
		for l in range(len(ls)):
			print(ls[l])
			sym = ls[l]['SYMBOL']
			fincode = ls[l]['FINCODE']
			with open('fincode.csv','a') as fl:
				writer = csv.writer(fl)
				writer.writerow([sym,fincode])


def spiderController(start, end):
	process = CrawlerProcess({
		"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
	})
	
	for i in range(start, end):
		process.crawl(MySpider, code=i)

	process.start()
	process.stop()


def duplicate():
	lines_seen = set() # holds lines already seen
	with open("fincode.csv", "r+") as f:
		d = f.readlines()
		f.seek(0)
		for i in d:
			if i not in lines_seen:
				f.write(i)
				lines_seen.add(i)
		f.truncate()

if __name__ == '__main__':
	#s = int(sys.argv[1])
	#e = int(sys.argv[2])
	s=132750
	e=132800
	spiderController(s,e)
	duplicate()
	sort()
