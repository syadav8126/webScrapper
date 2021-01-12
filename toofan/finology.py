# -*- coding: utf-8 -*-
import scrapy
import json
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import Crawler
from pandas import DataFrame
import io

class MySpider(scrapy.Spider):
	name = 'ntschools'
	start_urls = ['https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI']

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
			
	def parse(self, response, *args, **kwargs):

		url = 'https://ticker.finology.in/GetPrices.ashx?v=3.1&fincode=219300&stk=BSE&type=Y&count=1'
		url = 'https://ticker.finology.in/company/COALINDIA'
		#url = 'https://ticker.finology.in/GetValuation.ashx?v=3.1&fincode=219300&exc=BSE&top=365'
		#url = 'https://ticker.finology.in/Peers.ashx?v=3.1&fincode=219300&Mode=S'
		#url = 'https://ticker.finology.in/GetShares.ashx?v=3.1&fincode=219300'
		#url = 'https://ticker.finology.in/GetCorpAction.ashx?v=3.1&fincode=219300'
		#url = 'https://ticker.finology.in/News.ashx?v=3.1&fincode=219300'
		#url = 'https://ticker.finology.in/GetCompanybrief.ashx?v=3.1&fincode=219300'
		request = scrapy.Request(url, callback=self.parse_api, headers=self.headers)
		yield request

	def parse_api(self, response):
		raw_data = response.body
		raw_data = raw_data.decode('utf-8')
		data = pd.read_html(raw_data)
		frame = DataFrame(data)
		frame.to_csv(r'finologyconternt.csv',index = False, header=True)
		#y = json.loads(raw_data)
		#print(json.dumps(y, indent=4, sort_keys=True))

process = CrawlerProcess({
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
})

#process.crawl(MySpider,company_name='SBI',time_frame='frequency=3')
process.crawl(MySpider)
process.start()

