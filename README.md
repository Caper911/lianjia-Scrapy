# lianjia-Scrapy

* **抓取[东莞链家](https://dg.lianjia.com/zufang/)网站上的住房数据进行分析**
</br>
</br>

**知识总结**
1.**抓取下来的数据以json格式存储会乱码，需要在settings.py文件加上一行**
> FEED_EXPORT_ENCODING = 'utf-8' 

2.**使用选择器(Selector)**
> from scrapy.selector import Selector
> Selector(response).xpath('//span/text()').extract()

1. 可以使用上面这种方式来绑定选择器，也可以使用response的selector属性的xpath方法来实现
2. extract()方法用来提取文本,extract后会把selector对象转换成list类型<br>还可以使用extract_first()来获取第一个文本或者说提取到的唯一一个文本