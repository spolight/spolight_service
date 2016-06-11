from scrapy import Request, Spider
from scrapy.exceptions import CloseSpider


URL = 'http://info.nowgoal.cc/en/team/player.aspx?playerid={pid}'

class UrlSpider(Spider):
	handle_httpstatus_list = [404]
	name = "urlfinder"
	def start_requests(self):
		index = 27295
		while True:
			yield Request(URL.format(pid=index))
			index +=1
	
	def parse_url(self,response):
		if response.status == 404:
			raise CloseSpider("closed down")
		else:
			player_url = response.URL
			print '%s' %player_url

