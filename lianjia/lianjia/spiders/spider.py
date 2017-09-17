#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 13:16:19 2017

@author: caper911
@TargerUrl: https://dg.lianjia.com/zufang/
"""
import scrapy
from lianjia.items import LianjiaItem
from scrapy.http import Request
from scrapy.selector import Selector

class lianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ['dg.lianjia.com']
    start_urls = ['https://dg.lianjia.com/zufang/']
    j = 0
    #lianjia_url = 'https://dg.lianjia.com/zufang/' 
    #page_url = 'pg'
    
# =============================================================================
#     def start_requests(self):
#         for i in range(1,45):
#             url = self.lianjia_url+self.page_url+ str(i) +'/'
#             yield Request(url,self.parse)
#         
# =============================================================================
        
    def parse(self,response):
        selector = Selector(response)
        total_info = int(selector.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/h2/span/text()').extract()[0])
        max_page = int(selector.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/h2/span/text()').extract()[0]) // 30 + 1
        for i in range(1,max_page):
            url = self.start_urls[0] + 'pg' + str(i) +'/'
            #print(url)
            yield Request(url , callback=self.get_infomation , meta={'max_page':max_page,'total_info':total_info})
        
    
    def get_infomation(self,response):
        selector = Selector(response)
        item = LianjiaItem()
        
        
        total_info = response.meta['total_info']
        max_page = response.meta['max_page']
        list_num = 30
        
        if(self.j == max_page):
            list_num = (total_info - max_page*list_num) - 1
        
        self.j += 1
        for i in range(1,list_num):            
            item['title'] = selector.xpath('//*[@id="house-lst"]/li[' + str(i) +']/div[2]/h2/a/text()')\
                                .extract_first().replace(u'\xa0', u' ')  
            item['location'] = selector.xpath('//*[@id="house-lst"]/li['+ str(i) +']/div[2]/div[1]/div[1]/a/span/text()')\
                                .extract_first().replace(u'\xa0', u' ') 
            item['meters'] = selector.xpath('//*[@id="house-lst"]/li[' + str(i) +']/div[2]/div[1]/div[1]/span[2]/text()')\
                                .extract_first().replace(u'\xa0', u' ') 
            item['zone'] = selector.xpath('//*[@id="house-lst"]/li[' + str(i) +']/div[2]/div[1]/div[1]/span[1]/span/text()')\
                                .extract_first().replace(u'\xa0', u' ') 
            item['price'] = selector.xpath('//*[@id="house-lst"]/li['+ str(i) +']/div[2]/div[2]/div[1]/span/text()')\
                                .extract_first().replace(u'\xa0', u' ') 
            item['price_date'] = selector.xpath('//*[@id="house-lst"]/li[' + str(i) +']/div[2]/div[2]/div[2]/text()')\
                                .extract_first().replace(u'\xa0', u' ') 
            item['orientation'] = selector.xpath('//*[@id="house-lst"]/li['+ str(i) +']/div[2]/div[1]/div[1]/span[3]/text()')\
                                .extract_first().replace(u'\xa0', u' ') 
            yield item
        
