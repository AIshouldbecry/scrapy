# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobSpiderItem(scrapy.Item):
    title = scrapy.Field()
    job_city = scrapy.Field()
    job_classification = scrapy.Field()
    salary = scrapy.Field()
    experience_year = scrapy.Field()
    scrapy_time = scrapy.Field()
    publish_date = scrapy.Field()
    job_advantage_tags_list = scrapy.Field()
