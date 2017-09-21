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
        for i in range(1,max_page+1):
            url = self.start_urls[0] + 'pg' + str(i) +'/'
            #print(url)
            yield Request(url , callback=self.get_address_url , meta={'max_page':max_page,'total_info':total_info,'i':i})
        
    def get_address_url(self,response):
        selector = Selector(response)
        
        total_info = response.meta['total_info']
        max_page = response.meta['max_page']
        j = response.meta['i']
        list_num = 30

        if(j == max_page):
            list_num = (total_info - (max_page-1)*list_num)
        
        
        for i in range(1,list_num+1):  
      
        #//*[@id="house-lst"]/li[1]/div[2]/h2/a/@href 
            address_url = selector.xpath('//*[@id="house-lst"]/li['+ str(i) +']/div[2]/h2/a/@href')\
                                .extract_first()
            date = selector.xpath('//*[@id="house-lst"]/li[' + str(i) +']/div[2]/div[2]/div[2]/text()')\
                                .extract_first().replace(u'\xa0', u' ')
                                
            yield Request(address_url , callback=self.get_infomation , meta ={'date':date})
    
    
    def get_infomation(self,response):
        selector = Selector(response)
        item = LianjiaItem()
        
              
        #/html/body/div[4]/div[1]/div/div[1]/h1
        item['title'] = selector.xpath('/html/body/div[4]/div[1]/div/div[1]/h1/text()')\
                                .extract_first().replace(u'\xa0', u' ')  
        
        #/html/body/div[4]/div[2]/div[2]/div[2]/p[1]/text()
        item['meters'] = selector.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[1]/text()')\
                                .extract_first().replace(u'\xa0', u' ') 
        
        #/html/body/div[4]/div[2]/div[2]/div[2]/p[2]/text()
        item['zone'] = selector.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[2]/text()')\
                                .extract_first().replace(u'\xa0', u' ')
                                
        #/html/body/div[4]/div[2]/div[2]/div[1]/span[1]/text()
        item['price'] = selector.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/span[1]/text()')\
                                .extract_first().replace(u'\xa0', u' ') 
        
        item['price_date'] = response.meta['date'] 
        
        #/html/body/div[4]/div[2]/div[2]/div[2]/p[4]/text()
        item['orientation'] = selector.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[4]/text()')\
                                .extract_first().replace(u'\xa0', u' ')
        
        #/html/body/div[4]/div[2]/div[2]/div[2]/p[3]/text()
        item['floor'] = selector.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[3]/text()')\
                                .extract_first().replace(u'\xa0', u' ')
        
        #/html/body/div[4]/div[2]/div[2]/div[2]/p[7]/a[1]/text()                        
        item['urbanArea'] = selector.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[7]/a[1]/text()')\
                                .extract_first().replace(u'\xa0', u' ')
        
        #/html/body/div[4]/div[2]/div[2]/div[2]/p[7]/a[2]/text()                        
        item['streetName'] = selector.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[7]/a[2]/text()')\
                                .extract_first().replace(u'\xa0', u' ')
        
        #/html/body/div[4]/div[2]/div[2]/div[2]/p[6]/a[1]/text()
        item['housingEstate'] = selector.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[6]/a[1]/text()')\
                                .extract_first().replace(u'\xa0', u' ')
                                
        item['location'] = item['urbanArea'] + item['streetName'] + item['housingEstate']
                                
        yield item
        
