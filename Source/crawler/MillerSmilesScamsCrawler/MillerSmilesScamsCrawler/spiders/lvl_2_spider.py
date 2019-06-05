import scrapy
import re


def get_start_urls():
	result = []
	with open('lvl_1_urls.txt', 'r') as url_file:
		for url in url_file:
			result.append(url[:-1])
	return result


class Level2Spider(scrapy.Spider):
	name = 'lvl_2_spider'
	start_urls = get_start_urls()
	end_subjects = set()

	def parse(self, response):
		response = response.replace(body=response.body.replace(b'<br>', b' '))
		for subject in response.xpath('//b/a/text()').getall():
			self.end_subjects.add(subject.strip())

	def closed(self, reason):
		with open('lvl_2_subjects.txt', 'w') as subject_file:
			for subject in sorted(self.end_subjects):
				subject_file.write((subject + '\n').encode('utf-8'))