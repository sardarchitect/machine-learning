import scrapy


class QuotesSpider(scrapy.Spider):
    #SPIDER NAME
    name = 'scrapy_spider'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    #PARSING METHOD
    def parse(self, response):
        self.log('Visited: '+ response.url)
        for quote in response.css('div.quote'):
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract()
            }
            yield item

        #CRAWLING
        #Relative URL
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
               
        #NEW REQUEST
        if next_page_url:
            #Joins with home to create Absolute URL
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
