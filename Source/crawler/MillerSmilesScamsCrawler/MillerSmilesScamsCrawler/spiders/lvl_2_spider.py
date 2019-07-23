import scrapy
import re
import json


def get_start_urls():
	result = []
	with open('lvl_1_urls.txt', 'r') as url_file:
		for url in url_file:
			result.append(url[:-1])
	return result


class Level2Spider(scrapy.Spider):
	name = 'lvl_2_spider'
	start_urls = get_start_urls()
	end_emails = {'phishing_emails':[]}

	def parse(self, response):
		response = response.replace(body=response.body.replace(b'<br>', b' '))
		subjects = response.xpath('//b/a/text()').getall()
		bodies = response.xpath('//blockquote/p/font/text()').getall()
		for subject, body in zip(subjects, bodies):
			self.end_emails['phishing_emails'].append({'subject':subject, 'body':body})

	def closed(self, reason):
		with open('phishing_emails.json', 'w') as email_file:
			json.dump(self.end_emails, email_file)