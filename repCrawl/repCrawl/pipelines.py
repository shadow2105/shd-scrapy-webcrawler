# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# class scrapy.exporters.JsonItemExporter(file, **kwargs)
# file = the file-like object to use for exporting the data. Its write method should accept bytes
# can use any JSONEncoder __init__ method argument to customize this exporter.
from scrapy.exporters import JsonItemExporter


class RepcrawlPipeline:
    
    def __init__(self):
        self.exporter = None
        self.file = None

    # will be called to open the file (reps.json) when spider starts crawling.
    def open_spider(self, spider):
        self.file = open('reps.json', 'w+b')
        self.exporter = JsonItemExporter(self.file, indent=4, ensure_ascii=False)
        self.exporter.start_exporting()

    # will be called to close the file when spider is closed and scraping is over.
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    # will always be called (default), and
    # will be mainly responsible to convert the data to a specified format and print the data to the file.
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
