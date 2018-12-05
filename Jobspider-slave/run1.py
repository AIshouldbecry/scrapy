from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Jobspider.spiders.job_zhaopin import Jobpythonspider

def crawl(crawler, spider):
    crawler.crawl(spider)
    crawler.start()

if __name__ == '__main__':
    settings = get_project_settings()
    crawler = CrawlerProcess(settings)
    spider = Jobpythonspider()
    scheduler = BackgroundScheduler()
    scheduler.daemonic = False
    cron = CronTrigger(second='*/30')
    scheduler.add_job(crawl, cron,args=[crawler, spider])
    scheduler.start()
    while True:
        time.sleep(1000)