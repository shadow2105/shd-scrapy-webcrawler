# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RepcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    firstname = scrapy.Field()
    lastname = scrapy.Field()
    district = scrapy.Field()
    party = scrapy.Field()
    room = scrapy.Field()
    phone = scrapy.Field()
    committeeAssignment = scrapy.Field()
    type = scrapy.Field()
    country = scrapy.Field()
    url = scrapy.Field()

