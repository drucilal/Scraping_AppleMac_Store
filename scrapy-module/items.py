# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MacItem(scrapy.Item):
	name = scrapy.Field()
	rating = scrapy.Field()
	size = scrapy.Field()
	category = scrapy.Field()
	languages = scrapy.Field()
	compatibility = scrapy.Field()
	price = scrapy.Field()
