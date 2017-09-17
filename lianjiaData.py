#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:12:27 2017

@author: caper911
"""
import matplotlib.pyplot as plt
import pandas as pd
import json

fig = plt.figure(figsize=(10,6),dpi=80)

filePath = '/home/caper911/Scrapy/lianjia/lianjia/lianjia.json'

with open(filePath, 'r') as file:
    lianjia_info = json.load(file)


house_data = []

for item in lianjia_info:
    house_data.append( int(item['meters'].replace('平米  ','')))
    
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


