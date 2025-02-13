# CSS selectors

all_products = response.css('div.grid.grid--uniform.grid--collection').get()

name_of_product = response.css('.grid-product__title.grid-product__title--body::text').getall()
img_link_of product = response.css('img.grid-product__image::attr(src)').getall()
sale_price = response.xpath('//div[@class="grid-product__price"]/text()[normalize-space()]').getall()
