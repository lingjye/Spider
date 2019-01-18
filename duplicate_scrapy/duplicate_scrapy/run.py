#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
from multiprocessing import Process
from scrapy import cmdline
import datetime
import time

spiders = ['fengniaospider']

def start_spider(spider_name):
	while True:
		start_time = datetime.datetime.now()
		args = ['scrapy', 'crawl', spider_name]
		p = Process(target=cmdline.execute, args=(args,))
		p.start()
		p.join()

		clawer_time = datetime.datetime.now()
		wait_time = clawer_time - start_time
		print('结束:', clawer_time,'\n' '耗时:', wait_time)

		#等待下一天的11:00
		shold_start_date = datetime.date.today() + datetime.timedelta(days=1)
		next_date_str = '%s ' % shold_start_date + '11:00:00'
		next_date = datetime.datetime.strptime(next_date_str, '%Y-%m-%d %H:%M:%S')
		should_wait_time = next_date - datetime.datetime.now()
		time_stamp = should_wait_time.total_seconds()
		print('休眠:', time_stamp)
		time.sleep(time_stamp)

if __name__ == '__main__':
	# for spider in spiders:
    start_spider(spiders[0])
