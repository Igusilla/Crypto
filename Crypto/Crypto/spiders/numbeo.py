import scrapy

class NumbeoSpider(scrapy.Spider):
    name = "numbeo"

    def __init__(self):
        self.countries_data = {}

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2023",
            callback=self.parse_cost_of_living,
        )

    def parse_cost_of_living(self, response):
        for row in response.css('tbody tr'):
            country = row.css('td.cityOrCountryInIndicesTable::text').get()
            self.countries_data[country] = {
                'country': country,
                'cost_of_living_index': row.css('td::text').getall()[1],
                'purchasing_power_index': row.css('td::text').getall()[6],
                'quality_of_life_index': None,
                'safety_index': None,
            }
            
        yield scrapy.Request(
            url="https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=2023",
            callback=self.parse_quality_of_life,
        )

    def parse_quality_of_life(self, response):
        for row in response.css('tbody tr'):
            country = row.css('td.cityOrCountryInIndicesTable::text').get()

            if country in self.countries_data:
                self.countries_data[country]['quality_of_life_index'] = row.css('td::text').getall()[1]
                self.countries_data[country]['safety_index'] = row.css('td::text').getall()[3]
            else:
                self.countries_data[country] = {
                    'country': country,
                    'cost_of_living_index': None,
                    'purchasing_power_index': None,
                    'quality_of_life_index': row.css('td::text').getall()[1],
                    'safety_index': row.css('td::text').getall()[3],
                }

        for item in self.countries_data.values():
            yield item