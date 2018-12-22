# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from Jobspider.items import JobspiderItem, JobItemLoader
import time
from Jobspider.utils.common import get_md5
from datetime import datetime

class Jobpythonspider(RedisSpider):
    name = 'job_slave'
    redis_key ='requests'

    def parse(self,response):
        itemloader = JobItemLoader(item=JobspiderItem(), response=response)
        job_link = response.url
        job_name = response.xpath('//*[@class="job-name fl"]/text()')[0].extract()
        company = response.xpath('//*[@class="comp-name"]/text()')[0].extract()
        if response.xpath('//*[@class="add"]/text()'):
            address = response.xpath('//*[@class="add"]/text()').extract_first()
        else:
            address = '无'
        if response.xpath('//*[@class="about-main"]/p/text()'):
            job_info = ''.join(response.xpath('//*[@class="about-main"]/p/text()').extract())
        else:
            job_info = '无'
        salary = response.xpath('//*[@class="job-sal fr"]/text()')[0].extract()
        if response.xpath("//*[@class='tag']/text()"):
            job_tags = ';'.join(response.xpath("//*[@class='tag']/text()").extract())
        else:
            job_tags = '无'
        info1 = response.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[2]/span/text()')#判断工作时间的条件
        if info1:
            experience_year = response.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[2]/text()')[1].extract().rstrip()
        else:
            experience_year = response.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[2]/text()')[0].extract().lstrip().rstrip()
        if response.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[3]/text()')[0].extract().lstrip() == '':
            education_need = '学历不限'
        else:
            education_need  =response.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[3]/text()')[0].extract().lstrip().rstrip()
        itemloader.add_value("job_link", job_link)
        itemloader.add_value("job_name", job_name)
        itemloader.add_value("salary", salary)
        itemloader.add_value("company", company)
        itemloader.add_value("address", address)
        itemloader.add_value("job_info", job_info)
        itemloader.add_value("job_tags", job_tags)
        itemloader.add_value("experience_year", experience_year)
        itemloader.add_value("education_need", education_need)
        itemloader.add_value("crawl_time",datetime.now())
        item = itemloader.load_item()
        return item