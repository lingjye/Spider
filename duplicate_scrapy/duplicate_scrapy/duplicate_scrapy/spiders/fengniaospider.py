# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class FengniaospiderSpider(scrapy.Spider):
    name = 'fengniaospider'
    # allowed_domains = ['http://2.fengniao.com']
    start_urls = ['http://2.fengniao.com/price/add-1_1.html']#['http://www.baidu.com/'] #

    def parse(self, response):
        # return self.parse_content(response)
        start_url = 'http://2.fengniao.com/price/'
        # http://2.fengniao.com/price/def-1_1.html

        result_count = response.xpath('//div[@class="wrapper search-result"]/div[@class="result-count"]/em/text()').extract()[0]
        print('总数:',result_count)
        page = int(int(result_count) / 20) + 1
        print('总页数:', page)

        for i in range(1, 30): #(1, page + 1) 获取所有数据, 本例设置了延时,可以一定程度上解决被ban的概率
            url = start_url + 'add-1_%d.html' % (i)
            yield Request(url=url, callback=self.parse_content)

    def parse_content(self, response):

        items = []

        for each in response.xpath('//ul[@class="goods-list"]/li'):
            if len(each.xpath('div')) < 5:
                print('item相同')
                continue

            if each.xpath('@class') == 'goods-item clearfix': continue

            try:
                href = each.xpath('div[@class="cell-1"]/a/@href').extract()[0]
            except Exception as e:
                print('href查找失败',e);
                href = ''
            try:
                img = each.xpath('div[@class="cell-1"]/a/img/@data-original').extract()[0]
            except Exception as e:
                print('img查找失败',e);
                img = ''
            try:
                title = each.xpath('div[@class="cell-2"]/a[@class="goods-title"]/text()').extract()[0]
            except Exception as e:
                print('title查找失败',e);
                title = ''

            try:
                tag = each.xpath('div[@class="cell-2"]/div[@class="tags clearfix"]/a/text()').extract()[0]
            except Exception as e:
                print('tag查找失败',e);
                tag = ''

            try:
                city = each.xpath('div[@class="cell-2"]/div[@class="user-box clearfix"]/span[@class="city"]/text()').extract()[0]
            except Exception as e:
                print('city查找失败',e);
                city = ''

            try:
                quality = each.xpath('div[@class="cell-3"]/span[@class="quality-tag"]/text()').extract()[0]
            except Exception as e:
                print('quality查找失败',e);
                quality = ''

            try:
                price_info = each.xpath('div[@class="cell-4"]/div[@class="price-bar"]/span[@class="price-tag"]')
                price_unit = price_info.xpath('em[@class="unit"]/text()').extract()[0]
                price_text = price_info.xpath('em[@class="price"]/text()').extract()[0]
                price_decimal = price_info.xpath('em[@class="decimal-point"]/text()').extract()[0]
                price = price_unit + price_text + price_decimal
            except Exception as e:
                print('price查找失败',e);
                price = ''

            try:
                watch_count = each.xpath('div[@class="cell-5"]/div[@class="links"]/a[1]/text()').extract()[0]
            except Exception as e:
                print('watch_count查找失败', e);
                watch_count = ''
            try:
                message_count = each.xpath('div[@class="cell-5"]/div[@class="links"]/a[2]/text()').extract()[0]
            except Exception as e:
                print('message_count查找失败', e);
                message_count = ''
            try:
                links_info = each.xpath('div[@class="cell-5"]/div[@class="links"]')
                collect_count = links_info.xpath('span[@class="collect-count"]/text()').extract()[0]
            except Exception as e:
                print('collect_count查找失败', e);
                collect_count = ''

            try:
                post_time = links_info.xpath('p/text()').extract()[0]
            except Exception as e:
                print('post_time查找失败', e);
                post_time = ''

            item = {}
            item['href'] = href
            item['img'] = img
            item['title'] = title.strip()
            item['tag'] = tag.strip()
            item['city'] = city.strip()
            item['quality'] = quality
            item['price'] = price
            item['watch_count'] = watch_count
            item['message_count'] = message_count
            item['collect_count'] = collect_count
            item['post_time'] = post_time

            items.append(item)
            print(item)

        return items
