import scrapy

class WhiskeySpider(scrapy.Spider):
    name = 'computerp'
    start_urls = ['https://www.microcenter.com/category/4294966965/Desktop-Memory',
                ]

    def parse(self, response):
        for products in response.css('div.details'):
                itemnum = products.css('a.ProductLink_641292').attrib['data-id']

                yield {
                        'name' : products.css('a.ProductLink_'+itemnum+'::text').get(),
                        'price' : products.selector.xpath('/html/body/main/article/div[2]/article/ul/li[9]/div[2]/div/div[2]/div[1]/span/text()').get(),
                    }
      
      