# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib import parse
from JobSpider.items import JobSpiderItem
from bs4 import BeautifulSoup
from JobSpider.find_in_list import find_in_list
from datetime import datetime

class JobSpider(Spider):
    name = 'job'
    allowed_domains = ['search.51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html']

    def parse(self, response):
        # 1获取到每一条招聘的url并将url给具体的解析函数进行解析字段
        all_url = response.xpath('//*[@id="resultList"]//div/p/span/a/@href').extract()
        for one_url in all_url:
            yield Request(url=parse.urljoin(response.url, one_url), callback= self.parse_detail, dont_filter=True)

        # 2获取下一页的url并交给scrapy下载
        next_url = response.xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[8]/a/@href').extract_first("")
        if next_url:
            # yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)
            yield Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        item = JobSpiderItem()
        item['title'] = response.xpath("//div[@class='tHeader tHjob']//h1/text()").extract_first().strip()
        info = response.xpath("//p[@class='msg ltype']/@title").extract_first()
        item['job_city'] = info.strip().split("|")[0].strip()
        item['experience_year'] = find_in_list(self, key="经验", list_name=info)
        item['job_classification'] = response.xpath("//div[@class='mt10']/p[1]/span[2]/text()").extract_first("")
        item['salary'] = response.xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/strong//text()").extract_first("")
        item['scrapy_time'] = datetime.now()
        item['publish_date'] = find_in_list(self, key="发布", list_name=info)
        item['job_advantage_tags_list'] = response.xpath("//div[@class='t1']//span/text()").extract()
        yield item
        pass
