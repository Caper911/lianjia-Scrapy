# lianjia-Scrapy

* **抓取[东莞链家](https://dg.lianjia.com/zufang/)网站上的住房数据进行分析**
</br>
</br>

**知识总结**<br>
1.**抓取下来的数据以json格式存储会乱码，需要在settings.py文件加上一行**
> FEED_EXPORT_ENCODING = 'utf-8' 

2.**使用选择器(Selector)**
> from scrapy.selector import Selector<br>
Selector(response).xpath('//span/text()').extract()

1. 可以使用上面这种方式来绑定选择器，也可以使用response的selector属性的xpath方法来实现
2. extract()方法用来提取文本,extract后会把selector对象转换成list类型<br>还可以使用extract_first()来获取第一个文本或者说提取到的唯一一个文本

3.**使用pandas来处理数据** 
 > import pandas as pd
 area_level = [0, 50, 100, 150, 200, 250, 300, 500]    
y_labels = ['小于50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350']    
area_cut = pd.cut(house_data, area_level, labels=y_labels)

1. 将对应的数据按照area_level给定的区间进行聚类 得到一组用区间范围来表示的数据
2. 再使用相应的方法来计算，即可得到相应区间范围的数量。
>area_cut.value_counts()<br>
**value_counts()返回的是一个Series(pandas中的一个数据类型)，该数据类型包含着一个绘图方法plot()**
