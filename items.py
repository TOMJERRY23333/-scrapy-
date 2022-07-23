# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibouserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    comment=scrapy.Field()


class weiboimageItem(scrapy.Item):
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    # images = scrapy.Field()

class weibovideoItem(scrapy.Item):
    video_urls = scrapy.Field()
    video_paths = scrapy.Field()


