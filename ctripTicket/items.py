# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CtripticketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    flightCompany = scrapy.Field()#航空公司
    flightNumber = scrapy.Field()#航班号
    fromCity = scrapy.Field()#出发城市
    toCity = scrapy.Field()#到达城市
    flightDate = scrapy.Field()#出发日期
    leaveTime = scrapy.Field()#出发时间
    precision = scrapy.Field()#准点率
    price = scrapy.Field()#价格
    arriveDate= scrapy.Field()#到达日期
    pass
