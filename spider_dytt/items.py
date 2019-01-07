# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    host = scrapy.Field()
    classic = scrapy.Field()
    list_url = scrapy.Field()
    simpledesc = scrapy.Field()
    time = scrapy.Field()
    hot = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    download = scrapy.Field()

