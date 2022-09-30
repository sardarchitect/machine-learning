import scrapy


class QuotesSpider(scrapy.Spider):
    #SPIDER NAME
    name = 'authors'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    #PARSING METHOD
    def parse(self, response):
        urls = response.css('div.quote > span > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_auth_details)

        #CRAWLING
        #Relative URL
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
               
        #NEW REQUEST
        if next_page_url:
            #Joins with home to create Absolute URL
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
    def parse_auth_details(self, response):
        yield {
            'name': response.css('h3.author-title::text').extract_first(),
            'birth_date': response.css('span.author-born-date::text').extract_first()
        }