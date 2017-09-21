# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    #房子标题 
    title = scrapy.Field()
    
    #房子位置
    location = scrapy.Field()
    
    #房子的大小
    meters = scrapy.Field()
    
    #房子的格局
    zone = scrapy.Field()
    
    #价格
    price = scrapy.Field()
    
    #价格更新日期
    price_date = scrapy.Field()
    
    #房子朝向
    orientation = scrapy.Field()
    
    #城区名字
    urbanArea = scrapy.Field()
     
    #街道名称        
    streetName = scrapy.Field()
    
    #小区名字
    housingEstate = scrapy.Field()
    
    #高低中楼层
    floor = scrapy.Field()