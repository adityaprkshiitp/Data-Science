import scrapy
from quote.items import BookItem


class BookSpider(scrapy.Spider):
    name = "Book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.xpath("//article[@class = 'product_pod']")

        for book in books :
            title = response.xpath("./h3/a/@title").get()
            price = response.xpath("./div[@class = 'product_price']/p[@class = 'price_color']/text()").get() 
            review = response.xpath("./p[ contains(@class, 'star-rating')]/@class").get()
             
            print(title,price,review)
            bookItem = BookItem()
            bookItem["title"] = title
            bookItem["price"] = price
            bookItem["rating"] = review
