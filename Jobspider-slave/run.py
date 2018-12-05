from twisted.internet import reactor, defer
from Jobspider.spiders.job_zhaopin import Jobpythonspider
from Jobspider.spiders.job_zhaopin_ai import Jobaispider
#from Jobspider.spiders.job_zhaopin_bigdata import Jobbigdataspider
#from Jobspider.spiders.job_zhaopin_java import Jobjavaspider
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.blocking import  BlockingScheduler
from datetime import datetime

settings = get_project_settings()
configure_logging(settings)
runner = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl():

    yield runner.crawl(Jobaispider)
    yield runner.crawl(Jobpythonspider)
    reactor.stop()

#sched = BlockingScheduler()
#sched.add_job(crawl, 'date', run_date=datetime(2018, 12, 4, 11, 2, 55))  # 间隔时间触发
#sched.start()

crawl()
reactor.run()