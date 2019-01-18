# Spider
爬虫练习, 爬取蜂鸟二手商品信息

商品信息统一使用MongoDB数据库存储

主要商品信息如下:
```
#商品名称
'title':item['title'],
#商品链接
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
```
数据入库方式:
```
table.update({'href': item['href'], 'title':item['title']}, data, True);
```

duplicate_scrapy_test 是在Pycharm下创建的HTML5 Boilerplate工程, 用来测试duplicate_spider.py的自定义过滤(custome_dupefilter.py)规则

鉴于蜂鸟二手有反爬虫机制, 所以本例主要通过设置UserAgent和延时来解决, 当然也可以代理ip

###运行
通过scrapy crawl fengniaospider 或者 使用PyCharm运行run.py (也是引用了scrapy框架下的cmdline), 运行后爬虫会在每天的11:00自动开启

###注意
如要爬取所有二手数据, 请修改fengniaospider.py中的parse函数,如下:
```
#page+1, 代表要爬取的所有页码, 示例中为(1, 30)
for i in range(1, (1, page + 1):
    url = start_url + 'add-1_%d.html' % (i)
    yield Request(url=url, callback=self.parse_content)
```
