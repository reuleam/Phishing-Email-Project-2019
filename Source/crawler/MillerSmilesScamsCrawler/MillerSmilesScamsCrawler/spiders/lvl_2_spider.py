import scrapy


def get_start_urls():
	result = []
	with open('lvl_1_urls.txt', 'r') as url_file:
		for url in url_file:
			result.append('http://www.millersmiles.co.uk' + url[:-1])
	return result


class Level2Spider(scrapy.Spider):
	name = 'lvl_2_spider'
	start_urls = get_start_urls()
	end_urls = set()

	def parse(self, response):
		for url in response.xpath('//p/a/@href').getall():
			self.end_urls.add(url.strip())

	def closed(self, reason):
		print(self.end_urls)
		with open('lvl_2_urls.txt', 'w') as url_file:
			for url in sorted(self.end_urls):
				url_file.write((url + '\n').encode('utf-8'))