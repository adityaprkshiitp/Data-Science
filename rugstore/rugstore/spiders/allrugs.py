import scrapy


class AllrugsSpider(scrapy.Spider):
    name = "allrugs"
    allowed_domains = ["www.therugshop.com"]
    start_urls = ["https://www.therugshop.com/collections/medium"]

    def parse(self, response):
        for item in response.css('div.grid.grid--uniform.grid--collection'):
            yield {
                'name' : item.css('.grid-product__title.grid-product__title--body::text').get(),
                'img_link' : item.css('img.grid-product__image::attr(src)').get(),
                'price' : item.xpath('//div[@class="grid-product__price"]/text()[normalize-space()]').get(),
            }
        pass
