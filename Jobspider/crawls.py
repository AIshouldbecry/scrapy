# coding: utf8
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from werkzeug.utils import import_string, find_modules

scope = 'all'
process = CrawlerProcess(settings=get_project_settings())

for module_string in find_modules('Jobspider.spiders'):
    module = import_string(module_string)
    class_string = module_string.split('.')[-1].capitalize()+'spider'
    spider_class = getattr(module, class_string)
    process.crawl(spider_class, scope)

process.start()
