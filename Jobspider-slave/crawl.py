from Jobspider.spiders.job_zhaopin import Jobpythonspider
from Jobspider.spiders.job_zhaopin_ai import Jobaispider
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from datetime import datetime
from scrapy.crawler import CrawlerProcess

settings = get_project_settings()
configure_logging(settings)
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
process = CrawlerProcess(settings)
process.crawl(Jobpythonspider)
process.crawl(Jobaispider)
process.start()
process.stop()

