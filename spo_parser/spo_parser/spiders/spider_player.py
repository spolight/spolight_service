import scrapy

class PlayerSpider(scrapy.Spider):
	name = "player"
	start_urls = [
			"http://info.nowgoal.cc/en/team/player.aspx?playerid=27295"
			]

	def parse(self,response):
		player_info=response.xpath('//strong/text()').extract()
		name = player_info[0]
		country = player_info[1]
		weight = player_info[2]
		height = player_info[3]
		birth = player_info[4]
		foot = player_info[5]

		print "%s %s %s %s %s %s" %(name,country,weight,height,birth,foot)
		
