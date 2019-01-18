# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import datetime

class DuplicateScrapyPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            'title':item['title'],
            'href':item['href'],
            'img':item['img'],
            'tag':item['tag'],
            'city':item['city'],
            'quality':item['quality'],
            'price':item['price'],
            'watch_count':item['watch_count'],
            'message_count':item['message_count'],
            'collect_count':item['collect_count'],
            'post_time':item['post_time'],
            'add_time':datetime.datetime.now().strftime('%y%m%dT%H%M%S')
        }
        table = self.db[spider.name]
        # table.insert_one(data)
        table.update({'href': item['href'], 'title':item['title']}, data, True);
        return item

