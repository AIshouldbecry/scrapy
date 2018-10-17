# -*- coding: utf-8 -*-

# Scrapy settings for Jobspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Jobspider'

SPIDER_MODULES = ['Jobspider.spiders']
NEWSPIDER_MODULE = 'Jobspider.spiders'
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',

}
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 40
DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS_PER_DOMAIN =16
CONCURRENT_REQUESTS_PER_IP = 16
ITEM_PIPELINES = {
    'Jobspider.pipelines.JobspiderPipeline': 300,
}
