import scrapy


class Level1Spider(scrapy.Spider):
	name = 'lvl_1_spider'
	start_urls = [
		'http://www.millersmiles.co.uk/archives/current',
	]
	end_urls = set()

	def parse(self, response):
		for url in response.xpath('//p/a/@href').getall():
			self.end_urls.add(url.strip())

	def closed(self, reason):
		with open('lvl_1_urls.txt', 'w') as url_file:
			for url in sorted(self.end_urls):
				url_file.write(url + '\n')