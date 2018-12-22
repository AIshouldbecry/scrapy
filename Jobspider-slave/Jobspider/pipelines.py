# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class JobspiderPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient("154.8.168.28",27017)
        db = self.client["job_Jobspider_r_1"]
        self.collection = db["python"]

    def process_item(self, item, spider):
        content = dict(item)
        self.collection.insert(content)
        print("###################已经存入MongoDB########################")
        return item

    def close_spider(self,spider):
        self.client.close()
        pass


