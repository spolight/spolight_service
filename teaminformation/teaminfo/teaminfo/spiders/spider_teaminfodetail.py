import scrapy
from scrapy_splash import SplashRequest

class DmozSpider(scrapy.Spider):
    name = "teaminfodetail"
    #allowed_domains = ["dmoz.org"]
    start_urls = [
            "http://www.nowgoal.com/detail/1245738.html"
            ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args = {'wait': 0.5})

    def parse(self, response):
        """
        response.xpath('//tr/td[@style="text-align:right;"]/a/text()').extract()
        print response.xpath('//tr/td[@style="text-align:right;"]/a/text()').extract()
        """
        print response.xpath('//div[@id="home"]/a/span[@class="name"]/text()').extract() #hometeam
        print response.xpath('//div[@id="guest"]/a/span[@class="name"]/text()').extract() #guestteam
        print response.xpath('//span[@class="b t15"]/text()').extract() #hometeam score (needed to sperate)
        print response.xpath('//div[@id="matchData"]/div[7]/table[@class="bhTable"]/tbody/tr/td/text()').extract()
    

        """
        filename = response.url.split("/")[-2] + '2.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        """
