quote = response.css("div.quote span.text::text").get()
next = response.css("li.next a").get()

for books
books = response.xpath("//article[@class = 'product_pod']")
titles = response.xpath("//h3/a/@title").get()
prices = response.xpath("//div[@class = 'product_price']/p[@class = 'price_color']/text()").get() 
ratings = response.xpath("//p[ contains(@class, 'star-rating')]/@class").get()