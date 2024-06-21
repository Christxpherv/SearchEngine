import scrapy

class SimpleSpider(scrapy.Spider):
    name = "simple"
    start_urls = ['http://example.com']

    def parse(self, response):
        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, self.parse)
        yield {'title': response.css('title::text').get(), 'url': response.url}
