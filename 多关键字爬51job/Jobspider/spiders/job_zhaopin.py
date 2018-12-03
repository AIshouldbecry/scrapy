# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from Jobspider.utils.parse_detail import parse_detail_utils

class Jobpythonspider(scrapy.Spider):
    name = 'job_python'
    allowed_domains = ['m.zhaopin.com']
    # start_urls = ['https://m.zhaopin.com/hangzhou/']
    start_urls = ['https://m.zhaopin.com/beijing-530/?keyword=python&pageindex=1&maprange=3&islocation=0']
    base_url  = 'https://m.zhaopin.com/'

    def parse(self, response):
        print(response.url)
        # 这里是body 而不是text
        soup = BeautifulSoup(response.body,'lxml')
        all_sec = soup.find('div',class_='r_searchlist positiolist').find_all('section')
        for sec in all_sec:
            d_link = sec.find('a',class_='boxsizing')['data-link']
            detail_link = self.base_url+d_link
            if detail_link:
                yield scrapy.Request(detail_link,callback=self.parse_detail)

        # 是否有下一页的链接
        if soup.find('a',class_='nextpage'):
            next_url = self.base_url+soup.find('a',class_='nextpage')['href']
            print('next_url  ',next_url)
            # 若果有重复的，则不进行过滤
            yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)


    def parse_detail(self,response):
        yield parse_detail_utils(self, response)