# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpoParserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	# person info    
	person_name = scrapy.Field()
	age = scarpy.Field()
	country = scrapy.Field()
	foot = scrapy.Field()
	price = scrapy.Field()
	position = scrapy.Field()

	# Match info
	date = scrapy.Field()
	time = scrapy.Field()
	status = scrapy.Field()
	league = scrapy.Field()
	score = scrapy.Field()

	# Team info
	team_name = scrapy.Field()
	city = scrapy.Field()
	tgame_cnt = scrapy.Field()
	win_cnt = scrapy.Field()
	draw_cnt = scrapy.Field()
	lose_cnt = scrapy.Field()

	
	pass
