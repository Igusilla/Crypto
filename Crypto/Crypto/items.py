# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from attr import s
import scrapy


class TripleAItem(scrapy.Item):
    # define the fields for your item here like:
    country = scrapy.Field()
    population = scrapy.Field()
    ownership = scrapy.Field()
    ownership_percentage = scrapy.Field()
    
    pass

class NumbeoItem(scrapy.Item):
    country = scrapy.Field()
    cost_of_living_index = scrapy.Field()
    purchasing_power_index = scrapy.Field()
    quality_of_life_index = scrapy.Field()
    safety_index = scrapy.Field()
