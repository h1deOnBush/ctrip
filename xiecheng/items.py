# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 定义爬虫需要返回的字段
import scrapy



class XiechengItem(scrapy.Item):
    # define the fields for your item here like:

    # 城市表
    # 城市ID ok
    cityID = scrapy.Field()
    # 城市名称 ok
    cityName = scrapy.Field()
    # 景点个数 ok
    viewNum = scrapy.Field()


    # 城市网址（解析用 不输出）
    city_url = scrapy.Field()

    # 城市图片
    image1 = scrapy.Field()
    image2 = scrapy.Field()
    image3 = scrapy.Field()
    # 景点图片
    view_img1 = scrapy.Field()
    view_img2 = scrapy.Field()
    view_img3 = scrapy.Field()
    view_name = scrapy.Field()
    view_detail = scrapy.Field()