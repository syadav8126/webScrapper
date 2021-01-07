# -*- coding: utf-8 -*-
import scrapy
import json
import pandas as pd
from scrapy.crawler import CrawlerProcess


class MySpider(scrapy.Spider):
	name = 'ntschools'
	start_urls = ['https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI']

	headers = {
		":authority": "www.moneycontrol.com",
		":method": "GET",
		":path" : "/mc/widget/mcfinancials/getFinancialData?classic=true&referenceId=income&requestType=C&scId=SBI&frequency=3",
		":scheme": "https",
		"accept": "text/html, */*; q=0.01",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		"cookie": "A18ID=1610008424074.172164; _gcl_au=1.1.403021126.1610008424; _gid=GA1.2.1376170904.1610008432; _fbp=fb.1.1610008443020.310133732; _ga_4S48PBY299=GS1.1.1610008424.1.1.1610008474.0; _cb_ls=1; _cb=D3uI4UBv85_hCkNr7b; _chartbeat2=.1610008486968.1610008486968.1.DKBjdRD7utJf3eBXjCQtXrSLfLF4.1; _cb_svref=null; _ga=GA1.2.1669516111.1610008428; PHPSESSID=s9d434u492d287s5cdm64g77r4; _gat=1; __gads=ID=e21f4d1be11d1008-2286975396c500da:T=1610008596:RT=1610008596:S=ALNI_MaWGSPATQEqUDunZEye_yMs2_W5yw; GED_PLAYLIST_ACTIVITY=W3sidSI6IndrMXUiLCJ0c2wiOjE2MTAwMDg2MTgsIm52IjowLCJ1cHQiOjE2MTAwMDg0OTgsImx0IjoxNjEwMDA4NjEzfV0.; _chartbeat5=127,9308,%2Findia%2Fstockpricequote%2Fbanks-public-sector%2Fstatebankindia%2FSBI,https%3A%2F%2Fwww.moneycontrol.com%2Findia%2Fstockpricequote%2Fbanks-public-sector%2Fstatebankindia%2FSBI%23standalone,D3uZyYC1eqgKB91P6-GwTcH27lb,,c,CD2y0ID4rpzoIVj_dCWiselDBtExR,moneycontrol.com,::20,9337,%2Findia%2Fstockpricequote%2Fbanks-public-sector%2Fstatebankindia%2FSBI,https%3A%2F%2Fwww.moneycontrol.com%2Findia%2Fstockpricequote%2Fbanks-public-sector%2Fstatebankindia%2FSBI%23consolidated,D94ju4HEaErK97XKBy4uNrEyosc,,c,DPSJu4CmdLbkCrUXobD9mOVWBDjC5O,moneycontrol.com,::113,9405,%2Findia%2Fstockpricequote%2Fbanks-public-sector%2Fstatebankindia%2FSBI,https%3A%2F%2Fwww.moneycontrol.com%2Findia%2Fstockpricequote%2Fbanks-public-sector%2Fstatebankindia%2FSBI%23income_statement,BVzAYDDCl4SPBc-xJyDnHui4Cj2YdM,,c,BpL24-DwedD3BzoD_VCRvYcTB6SdLl,moneycontrol.com",
		"dnt": "1",
		"referer": "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		"x-requested-with": "XMLHttpRequest"
	}

	def parse(self, response):

		url = 'https://www.moneycontrol.com/mc/widget/mcfinancials/getFinancialData?classic=true&referenceId=income&requestType=S&scId=SBI&frequency=3'
		request = scrapy.Request(url, callback=self.parse_api, headers=self.headers)
		yield request

	def parse_api(self, response):
		raw_data = response.body
		raw_data = raw_data.decode('utf-8')
		data = pd.read_html(raw_data)
		print(data)

process = CrawlerProcess({
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
})

process.crawl(MySpider)
process.start()


