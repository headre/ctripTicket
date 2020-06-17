# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from ctripTicket.settings import MYSQL_DATABASE,MYSQL_URI
import pymysql.cursors
class CtripticketPipeline(object):
    def __init__(self):
        self.mysql_url = MYSQL_URI
        self.mysql_db = MYSQL_DATABASE

    def open_spider(self, spider):
        self.mysql_conn = pymysql.connect(
            host=self.mysql_url,
            user="root",
            db=self.mysql_db,
            password="2333",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

    def process_item(self, item, spider):
        try:
            with self.mysql_conn.cursor() as cursor:

                # define the fields for your item here like:
                # name = scrapy.Field()
                flightCompany = item.get("flightCompany","")  # 航空公司
                flightNumber = item.get("flightNumber","")  # 航班号
                fromCity = item.get("fromCity","")  # 出发城市
                toCity = item.get("toCity","")  # 到达城市
                flightDate = item.get("flightDate","")  # 出发日期
                leaveTime = item.get("leaveTime","")  # 出发时间
                precision = item.get("precision","") # 准点率
                price = item.get("price","")  # 价格
                arriveDate = item.get("arriveDate","")  # 到达日期

                route_search = "SELECT* FROM `routelist` WHERE `fcity`=%s AND `tcity`=%s AND `flightDate`=%s AND `airlineCompany`=%s AND `flightNumber`=%s AND `precision`=%s AND `price`=%s AND `arriveDate`=%s AND `leaveTime`=%s"
                cursor.execute(route_search,(fromCity,toCity,flightDate,flightCompany,flightNumber,precision,price,arriveDate,leaveTime))
                routeIsExist = cursor.fetchone()

                if routeIsExist is None:
                    sql_write = "INSERT INTO `routelist` (`fcity`,`tcity`,`flightDate`,`airlineCompany`,`flightNumber`,`precision`,`price`,`arriveDate`,`leaveTime`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql_write, (fromCity,toCity,flightDate,flightCompany,flightNumber,precision,price,arriveDate,leaveTime))

            self.mysql_conn.commit()

        except Exception as e:
            print(e)
            pass
        return item

    def close_spider(self, spider):
        self.mysql_conn.close()