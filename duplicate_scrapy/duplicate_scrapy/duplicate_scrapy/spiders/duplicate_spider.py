# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from duplicate_scrapy.items import DuplicateScrapyItem

class DuplicateSpiderSpider(scrapy.Spider):
    name = 'duplicate_spider'
    # allowed_domains = ['duplicate_scrapy']
    start_urls = ['http://localhost:63342/duplicate_scrapy_test/src/index.html']

    def parse(self, response):

        items = []

        for each in response.xpath('//a'):
            print('解析第一部分')
            title = each.xpath('text()').extract()[0]
            href = each.xpath('@href').extract()[0]

            item = DuplicateScrapyItem()
            item['title'] = title
            item['href'] = href
            item['description'] = ''

            items.append(item)

            print(title)
            print(href)


        for item in items:

            url = 'http://localhost:63342/duplicate_scrapy_test/src/' + item['href']

            yield Request(url=url, meta={'item':item},callback=self.parse_Description)

        return items

    def parse_Description(self, response):
        print('解析第二部分')
        item = response.meta['item']
        description = response.xpath('//title/text()').extract()[0]
        item['description'] = description
        return item
