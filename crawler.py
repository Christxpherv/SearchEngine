import scrapy

class SimpleSpider(scrapy.Spider):
    name = "simple"
    start_urls = ['http://example.com']

    def parse(self, response):
        # Extract the content from the <body> tag
        content = ' '.join(response.css('body *::text').getall())
        
        # Yield a dictionary with 'title', 'url', and 'content' keys
        yield {
            'title': response.css('title::text').get(),
            'url': response.url,
            'content': content.strip()  # Store content as a string
        }

        for href in response.css('a::attr(href)').getall():
            # Call the parse method for each link
            yield response.follow(href, self.parse)
