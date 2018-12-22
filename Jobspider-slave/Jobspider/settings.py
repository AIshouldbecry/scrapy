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
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 40
DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT=4
CONCURRENT_REQUESTS=16 #所拿取request数量
COOKIES_ENABLED = False
ITEM_PIPELINES = {
    'Jobspider.pipelines.JobspiderPipeline': 300,
    #'scrapy_redis.pipelines.RedisPipeline': 301
}
DOWNLOADER_MIDDLEWARES = {
    'Jobspider.timeout_middleware.Timeout_Middleware':610,
    'Jobspider.useragent.RotateUserAgentMiddleware':400
}
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True

SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_URL = 'redis://root:foobared@39.106.14.176:6379'
