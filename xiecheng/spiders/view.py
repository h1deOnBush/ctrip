# -*- coding: utf-8 -*-
import scrapy
import re
from xiecheng.items import XiechengItem
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.spiders import Spider


class ViewSpider(scrapy.Spider):
    name = 'view'
    allowed_domains = ['ctrip.com']
    start_urls = ['https://you.ctrip.com/place/']
    baseurl = "https://you.ctrip.com"

    def parse(self, response):
        """获取地区url"""
        cityNames = response.xpath('//div[@id="journals-panel-items"]/dl[1]/dd[@class="panel-con"]/ul/li/a')
        for each_cityNames in cityNames:
            item = XiechengItem()
            item['city_url'] = ','.join(each_cityNames.xpath('@href').extract())

            city_url = self.baseurl + item['city_url']
            yield scrapy.Request(city_url, callback=self.getcityInfo)
            yield item

    def getcityInfo(self, response):
        """地区名称 图片链接 景点链接"""
        item = XiechengItem()
        # 城市名称
        cityName = response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/h1/a/@title').get()
        item['cityName'] = cityName

        # image_url = response.xpath('/html/body/div[4]/div[1]/div[2]/div[1]/a//@href').get()
        # scrapy.Request(image_url)

        item['image1'] = self.baseurl + str(response.xpath(
            '/html/body/div[4]/div[1]/div[2]/div[1]/div[3]/div[1]/a/@href').get())
        item['image2'] = self.baseurl + response.xpath(
            '/html/body/div[4]/div[1]/div[2]/div[1]/div[3]/div[2]/a/@href').get()
        item['image3'] = self.baseurl + response.xpath(
            '/html/body/div[4]/div[1]/div[2]/div[1]/div[3]/div[3]/a/@href').get()

        view_list = response.xpath('//*[@id="poi_0"]/ul//@href')
        for view in view_list:
            view_url = self.baseurl + view.get()
            yield scrapy.Request(view_url, callback=self.getviewInfo)

    def getviewInfo(self, response):
        """景点相关"""
        item = XiechengItem()
        view_name = response.xpath('/html/body/div[2]/div[1]/ul/li[3]/h1/text()').get()
        view_img1 = response.xpath('//*[@id="detailCarousel"]/div/div[1]/a/img/@src').get()
        view_img2 = response.xpath('//*[@id="detailCarousel"]/div/div[2]/a/img/@src').get()
        view_img3 = response.xpath('//*[@id="detailCarousel"]/div/div[3]/a/img/@src').get()
        view_detail = response.xpath('/html/body/div[3]/div/div[1]/div[5]/div[2]/div[1]/div/text()').get()
        item['view_name'] = view_name
        item['view_img1'] = view_img1
        item['view_img2'] = view_img2
        item['view_img3'] = view_img3
        item['view_detail'] = view_detail

        yield item
