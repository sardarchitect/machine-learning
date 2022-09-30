import json
import scrapy


class QuotesSpider(scrapy.Spider):
    #SPIDER NAME
    name = 'authors'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

    #PARSING METHOD
    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield{
                'author_name': quote['author']['name'],
                'text': quote['text'],
                'tags': quote['tags']
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)