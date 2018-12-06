# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
#from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from Jobspider.utils.InsertRedis import inserintotc, inserintota

class Jobpythonspider(scrapy.Spider):
    name = 'job_python'
    # start_urls = ['https://m.zhaopin.com/hangzhou/']
    start_urls = ['https://m.zhaopin.com/beijing-530/?keyword=python&pageindex=1&maprange=3&islocation=0']
    base_url  = 'https://m.zhaopin.com'

    def parse(self, response):
        soup = BeautifulSoup(response.body,'lxml')
        all_sec = soup.find('div',class_='r_searchlist positiolist').find_all('section')
        for sec in all_sec:
            d_link = sec.find('a',class_='boxsizing')['data-link']
            detail_url = self.base_url+d_link
            if detail_url:
                inserintota(detail_url,2)
                print('########the detail link: ' + detail_url + ' is insert into the redis queue#######')

        if soup.find('a', class_='nextpage'):
            next_url = self.base_url + soup.find('a', class_='nextpage')['href']
            if next_url:
                inserintotc(next_url,1)
                print("########the next link: " + next_url + " is insert into the redis queue#########")
                yield Request(next_url, callback=self.parse,dont_filter=True)
