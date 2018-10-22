# -*- coding: utf-8 -*-

# Scrapy settings for JobSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
BOT_NAME = 'JobSpider'
SPIDER_MODULES = ['JobSpider.spiders']
NEWSPIDER_MODULE = 'JobSpider.spiders'
CONCURRENT_REQUESTS = 40
DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS_PER_DOMAIN =16
CONCURRENT_REQUESTS_PER_IP = 16
ITEM_PIPELINES = {
    'JobSpider.pipelines.JobSpiderPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline':301
}
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.51job.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
FEED_EXPORT_ENCODING = 'utf-8'
ROBOTSTXT_OBEY = False
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#去重
REDIS_URL = 'redis://root:foobared@39.106.14.176:6379'
