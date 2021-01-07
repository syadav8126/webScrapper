# -*- coding: utf-8 -*-
import scrapy
import json


class NtschoolsSpider(scrapy.Spider):
	name = 'ntschools'
	start_urls = ['https://directory.ntschools.net/#/schools']

	headers = {
	"Accept":"application/json",
	"Accept-Encoding":"gzip, deflate, br",
	"Accept-Language":"en-US,en;q=0.5",
	"Referer": "https://directory.ntschools.net/",
	"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
	"X-Requested-With": "Fetch"
	}

	def parse(self, response):
		url = 'https://directory.ntschools.net/api/System/GetAllSchools'

		request = scrapy.Request(url, callback=self.parse_api, headers=self.headers)
		yield request
	
	def parse_api(self, response):
		base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
		raw_data = response.body
		data = json.loads(raw_data)
		for school in data:
			school_code = school['itSchoolCode']
			school_url = base_url+school_code
			request = scrapy.Request(school_url, callback=self.parse_school, headers=self.headers)
			yield request

	def parse_school(self, response):
		raw_data = response.body
		data = json.loads(raw_data)
		print("---------------------")
		print(data)
		yield{
			'Name':data['name'],
			'Email':data['mail'],
			'Phone':data['telephoneNumber']
		}
