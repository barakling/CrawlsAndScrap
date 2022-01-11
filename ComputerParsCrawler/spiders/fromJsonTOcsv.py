import scrapy
import json
class WebCrawl(scrapy.Spider):
    name = "spooder"
    allowed_domains = ["thestar.com.my"]
    start_urls = ["https://cdn.thestar.com.my/Content/Data/parsely_data.json"]
    def parse(self, response):
        yield from json.loads(response.text)['data']

   