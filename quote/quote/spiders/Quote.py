import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

# Using CrawlSpider
# class QuoteSpider(CrawlSpider):
#     name = "Quote"
#     allowed_domains = ["quotes.toscrape.com"]
#     start_urls = ["https://quotes.toscrape.com/"]
#     rules = [Rule(LinkExtractor(allow= 'page/', deny= 'tag/'), callback = 'parse', follow= True)]

#     def parse(self, response):
#         for quote in response.css("div.quote span.text::text"):
#             yield {
#                 "quote" : quote.get()
#             }

# Spider made to follow next link
class QuoteSpider(scrapy.Spider):
    name = "Quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]
 
    def parse(self, response):
        for next_page in response.css("li.next a") : 
            yield response.follow(next_page, self.parse)

        for quote in response.css("div.quote span.text::text"):
            yield {
                "quote" : quote.get()
            }

            
