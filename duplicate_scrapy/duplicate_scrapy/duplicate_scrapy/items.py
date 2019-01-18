# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DuplicateScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    img = scrapy.Field()
    tag = scrapy.Field()
    city = scrapy.Field()
    quality = scrapy.Field()
    price = scrapy.Field()
    watch_count = scrapy.Field()
    message_count = scrapy.Field()
    collect_count = scrapy.Field()
    post_time = scrapy.Field()

    pass
