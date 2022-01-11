import scrapy

class WebCrawl(scrapy.Spider):
    name = "moretvscreens"
    allowed_domains = ["croma.com"]
    start_urls = []
    for x in range(1,500):
        start_urls.append(f"https://www.croma.com/televisions-accessories/led-tvs/large-screen-tvs/c/{x}")

    def parse(self, response):        
        for items in response.css('div.cp-product'):
            yield {
                    'name' : items.xpath('//div[2]/div[1]/h3/a/text()').get(),
                    'price' :items.css('span.amount::text').get().replace('₹',''),
                }

    #check start_urls
    #print(start_urls)