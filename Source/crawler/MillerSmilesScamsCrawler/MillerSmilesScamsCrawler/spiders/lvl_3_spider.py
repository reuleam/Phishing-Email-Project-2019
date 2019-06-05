import scrapy


def get_start_urls():
	result = []
	with open('lvl_2_urls.txt', 'r') as url_file:
		for url in url_file:
			result.append('http://www.millersmiles.co.uk' + url[:-1])
	return result


class Level3Spider(scrapy.Spider):
	name = 'lvl_3_spider'
	start_urls = get_start_urls()
	end_subjects = set()

	def parse(self, response):
		response = response.replace(body=response.body.replace(b'<br>', b' '))
		for subject in response.xpath('//b/a/text()').getall():
			self.end_subjects.add(subject.strip())

	def closed(self, reason):
		print(self.end_subjects)
		with open('lvl_3_subjects.txt', 'w') as subject_file:
			for subject in sorted(self.end_subjects):
				subject_file.write((subject + '\n').encode('utf-8'))