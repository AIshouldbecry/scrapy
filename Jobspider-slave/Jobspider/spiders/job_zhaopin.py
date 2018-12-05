# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from Jobspider.items import JobspiderItem, JobItemLoader
import time
from Jobspider.utils.common import get_md5

class Jobpythonspider(RedisSpider):
    name = 'job_slave'
    redis_key ='requests'

    def parse(self,response):
        itemloader = JobItemLoader(item=JobspiderItem(), response=response)
        job_link = response.url
        job_id = get_md5(job_link + str(int(time.time())))
        job_name = response.xpath('//*[@class="job-name fl"]/text()')[0].extract()
        company = response.xpath('//*[@class="comp-name"]/text()')[0].extract()
        address = response.xpath('//*[@class="add"]/text()').extract_first()
        job_info = ''.join(response.xpath('//*[@class="about-main"]/p/text()').extract())
        salary = response.xpath('//*[@class="job-sal fr"]/text()')[0].extract()
        job_tags = ';'.join(response.xpath("//*[@class='tag']/text()").extract())
        itemloader.add_value("job_link", job_link)
        itemloader.add_value("job_id", job_id)
        itemloader.add_value("job_name", job_name)
        itemloader.add_value("salary", salary)
        itemloader.add_value("company", company)
        itemloader.add_value("address", address)
        itemloader.add_value("job_info", job_info)
        itemloader.add_value("job_tags", job_tags)
        item = itemloader.load_item()
        return item