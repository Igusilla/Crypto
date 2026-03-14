# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripleAItem(scrapy.Item):
    # define the fields for your item here like:
    country = scrapy.Field()
    population = scrapy.Field()
    ownership = scrapy.Field()
    ownership_percentage = scrapy.Field()
    
    pass
