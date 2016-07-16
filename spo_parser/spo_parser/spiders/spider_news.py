import scrapy

class News_Spider(scrapy.Spider):
	name = "news"
	start_urls = [
			"http://www.espnfc.com/italian-serie-a/12/index",
			"http://www.espnfc.com/english-premier-league/23/index",
			"http://www.espnfc.com/spanish-primera-division/15/index",
			"http://www.espnfc.com/german-bundesliga/10/index",
			"http://www.espnfc.com/french-ligue-1/9/index"
			]

	def parse(self, response):
		headline=response.xpath('//article/h1/a/text()').extract()
		image=response.xpath('//div[contains(@class,"picture")]/img/@src').extract()
		author=response.xpath('//div[contains(@class,"author")]/a/text()').extract()
		upload_date=response.xpath('//div[contains(@class,"publish-date")]/time/@datetime').extract()
