import scrapy
from scrapy_splash import SplashRequest

class DmozSpider(scrapy.Spider):
    name = "teaminfo"
    #allowed_domains = ["dmoz.org"]
    start_urls = [
            "http://www.nowgoal.com/schedule.htm?f=sc&date=2016-6-2"
            ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args = {'wait': 0.5})

    def parse(self, response):
        
        """
        response.xpath('//tr/td[@style="text-align:right;"]/a/text()').extract()
        print response.xpath('//tr/td[@style="text-align:right;"]/a/text()').extract()
        """
        print response.xpath('//tr/td[@class="red"]/@onclick').extract()
        #teamID_number DB extract
        
        """
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        """
