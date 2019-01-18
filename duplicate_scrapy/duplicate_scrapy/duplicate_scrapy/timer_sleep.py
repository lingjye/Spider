#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

import datetime
import time


def run_sleep():
	start_time = datetime.datetime.now()
	time.sleep(2)
	end_time = datetime.datetime.now()
	wait_time = end_time - start_time
	print('等待:', wait_time)
	print('等待时间戳差:', datetime_toTimestamp(end_time))
	shold_start_date = datetime.date.today() + datetime.timedelta(days=1)
	next_date = '%s ' % shold_start_date + '09:00:00'
	print(next_date)

	next_date = string_toDatetime(next_date, '%Y-%m-%d %H:%M:%S')

	print(shold_start_date, next_date)


	should_wait_time = next_date - end_time
	time_stamp = should_wait_time.total_seconds()
	print('还需等待:', type(wait_time), wait_time.total_seconds(), time_stamp)


#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")

#把字符串转成datetime
def string_toDatetime(string, format="%Y-%m-%d-%H:%M:%S"):
    return datetime.datetime.strptime(string, format)

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return string_toDatetime(strTime).timetuple()

#把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))

#把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTim):
    return dateTim.timetuple()


if __name__ == '__main__':
    run_sleep()