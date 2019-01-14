# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 管道：数据清洗、去重
# 持久化：写txt、csv。写入数据库

# scrapy框架将爬取spider模块和处理层pipeline分离开，使得程序更容易扩展
# spider yield 生成的item会交给pipeline处理，如果爬取速度跟处理速度不一致的话，scrapy框架会自动调度
# spider yield 相当于生产消费模型中的生产者，pipeline相当于消费者。如果爬取解析速度快于pipeline，那么还没来得及处理的item会进入队列当中(item_chain)。

class MoviePipeline(object):
    def process_item(self, item, spider):
        # 爬虫部分在for循环中yield item，所以process_item方法会重复执行
        # open(mode="a") 追加模式，如果w模式的话会覆盖掉上次写的信息
        with open('my_meiju.txt', 'a', encoding='utf-8') as f:
            # 把对象，封装成了字典
            f.write(str(item['name']) + '\n')
            # 相对路径直接生成在项目的跟目录下，不是相对目录，建议用绝对路径
        return item
