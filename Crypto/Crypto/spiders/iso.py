import scrapy

class ISOSpider(scrapy.Spider):
    name = 'iso'
    start_urls = ['https://www.iban.com/country-codes']
    
    def parse(self, response):
        for row in response.css('tbody tr'):
            yield {
                'country': row.css('td::text').getall()[0],
                'iso': row.css('td::text').getall()[2],
            }