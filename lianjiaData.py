#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:12:27 2017

@author: caper911
"""
import matplotlib.pyplot as plt
import pandas as pd
import json
import requests
import numpy as np

fig = plt.figure(figsize=(10,6),dpi=80)

filePath = '/home/caper911/Scrapy/lianjia/lianjia/lianjia.json'

with open(filePath, 'r') as file:
    lianjia_info = json.load(file)


house_data = []
house_address = []
house_price = []

for item in lianjia_info:
    house_data.append( int(item['meters'].replace('平米  ','')))
    house_price.append(int(item['price']))
    house_address.append({'address':"{}".format(item['location']),'lat':'','lng':''})
    
#print(house_address)
#####
#将房子出租位置地址转成相应的纬度坐标

# =============================================================================
# headers = {
#         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36',
#         'Accept-Language':'zh-CN,zh;q=0.8'
#         }
# for i in range(0,len(house_address)):
#     
#     address = house_address[i]['address']
#     addressUrl = "http://maps.googleapis.com/maps/api/geocode/json?address=" + address
# 
#     html = requests.get(addressUrl, headers = headers)
#     MapJson = json.loads(html.text)
#     
#     if MapJson.get('status')=="OK":
#         house_address[i]['lat'] = MapJson.get('results')[0]['geometry']['location']['lat']  
#         house_address[i]['lng'] = MapJson.get('results')[0]['geometry']['location']['lng']  
#     else:
#         continue
# 
# =============================================================================
#print(address +':')
print( house_address)  


###############################
#房屋出租面积分析

area_level = [0, 50, 100, 150, 200, 250, 300, 500]    
y_labels = ['小于50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350']    

area_cut = pd.cut(house_data, area_level, labels=y_labels)
#print(area_cut)


#value_counts()返回的是一个Series(pandas中的一个数据类型)，该数据类型包含着一个绘图方法plot()
# alpha = 0.4 频率分布图的透明度
# kind = bar 类型是柱状图
# grid = True  是否显示网格背景
area_cut.value_counts().plot(kind='bar',color = "blue", rot=25, alpha=1.0, grid=True, fontsize='12')
    
#print(area_cut.value_counts())


plt.title('房屋出租面积分布')    
plt.xlabel('面积(㎡)')
#plt.ylabel('户数')    
plt.legend(['数量']) 
plt.show()


###############################
#房屋出租价格分布分析

#设置生成图片大小
fig = plt.figure(figsize=(10,6),dpi=80)
#price_level = np.linspace(min(house_price),max(house_price)+1,11)
#print(price_level)

price_level = [400,1000,1800,2500,3300,4700,6200,7700,15000]

price_labels = ['400-1000','1000-1800' ,'1800-2500', '2500-3300' , '3300-4700', '4700-6200', '6200-7700', '7700-15000']
price_area_cut = pd.cut(house_price, price_level, labels=price_labels)

price_area_cut.value_counts().plot(kind='bar',color = "blue", rot=25, alpha=1.0, grid=True, fontsize='12')

plt.title('房屋出租价格分布分析')    
plt.xlabel('货币单位:元')
#plt.ylabel('户数')    
plt.legend(['数量']) 
plt.show()


