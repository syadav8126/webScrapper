# -*- coding: utf-8 -*-
import scrapy
import json
import pandas as pd
from scrapy.crawler import CrawlerProcess


class MySpider(scrapy.Spider):
	name = 'ntschools'
	start_urls = ['https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI']

	headers = {
		"accept": "text/html, */*",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		"content-length": "0",
		"content-type": "text/plain",
		"dnt": "1",
		"referer": "https://www.moneycontrol.com",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "cross-site",
		"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		"x-requested-with": "XMLHttpRequest"
	}

	def parse(self, response):

		url = 'https://www.moneycontrol.com/india/stockpricequote/'
		request = scrapy.Request(url, callback=self.parse_api, headers=self.headers)
		yield request

	def parse_api(self, response):
		raw_data = response.body
		raw_data = raw_data.decode('utf-8')
		p = pd.read_html(raw_data)
		print(p)

process = CrawlerProcess({
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
})

process.crawl(MySpider)
process.start()


