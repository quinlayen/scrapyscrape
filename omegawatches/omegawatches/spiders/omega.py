import scrapy
import json
from scrapy_selenium import SeleniumRequest

class OmegaSpider(scrapy.Spider):
    name = "omega"
    allowed_domains = ["omegawatches.com"]
    

    def start_requests(self):
        start_url = "https://www.omegawatches.com/en-us/watchfinder"
        yield SeleniumRequest(url=start_url, 
                              callback=self.parse, 
                              wait_time=2, 
                              script='window.scrollTo(0, document.body.scrollHeight);'
                             )
        
    def parse(self, response):
        pass
