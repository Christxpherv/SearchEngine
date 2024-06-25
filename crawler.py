import scrapy

class SimpleSpider(scrapy.Spider):
    name = "simple"
    start_urls = ['http://example.com']

    def parse(self, response):
        # Extract the content from the <body> tag and clean it up
        content = ' '.join(response.css('body *::text').getall())
        cleaned_content = ' '.join(content.split())  # Remove extra whitespace and newlines
        
        # Yield a dictionary with 'title', 'url', and 'content' keys
        yield {
            'title': response.css('title::text').get(),
            'url': response.url,
            'content': cleaned_content 
        }

        # Follow all links on the page
        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, self.parse)
