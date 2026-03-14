import scrapy

class CryptoAdoptionPerCountry(scrapy.Spider):
    name = "triple_a"
    start_urls = ['https://www.triple-a.io/cryptocurrency-ownership-data']
    
    def parse(self, response):
        for country in response.css('div.table-row.w-dyn-item'):
            yield {
                'name': country.css('div.text-size-regular::text').get(),
                'population': country.css('div.table-item._15 div.text-size-small::text').getall()[0].strip(),
                'ownership': country.css('div.table-item._25 div.text-size-small::text').get().strip(),
                'ownership_percentage': country.css('div.table-item._15 div.text-size-small::text').getall()[1].strip(), 
            }
        
        next_page = response.css('a.w-pagination-next.pagination-button').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
