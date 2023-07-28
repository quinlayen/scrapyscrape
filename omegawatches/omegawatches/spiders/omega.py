import scrapy
import os
import json
# from scrapfly import ScrapeConfig
# from scrapfly.scrapy import ScrapflyMiddleware, ScrapflyScrapyRequest, ScrapflySpider, ScrapflyScrapyResponse
from ..items import WatchItem
# #from selenium.webdriver import Chrome
# from selenium import webdriver
# # from scrapy_selenium import SeleniumRequest
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('SCRAPFLY_API_KEY')


class OmegaSpider(scrapy.Spider):
    name = "omega"
    allowed_domains = ["omegawatches.com"]
    start_urls = ["https://www.omegawatches.com/en-us/watchfinder?p=72"]
    
  
    
    def parse_img_urls(self, images):
        image_list = images.split(" ")
        return image_list[-2]
        
    def parse(self, response):
        item = WatchItem()
        watches = response.xpath('//li[@class="product-item"]')
        for watch in watches:
            item['watch_url'] = watch.xpath('.//a[@class="ow-prod__img"]/@href').get(),
            item['image_urls'] = self.parse_img_urls(watch.xpath('.//a[@class="ow-prod__img"]/picture/source/@data-srcset').get()),
            item['watch_price'] = watch.xpath('.//span[@class="price"]/text()').get()     
            yield item
  
  
  
  
  
  
    '''  This is for getting entire html.
      # def parse(self, response):
    #     for href in response.xpath('//li[@class="product-item"]//a[@class="ow-prod__img"]/@href').getall():
    #         yield scrapy.Request(href, callback=self.parse_watches)

     
    # def parse_watches(self, response):
    #     item = WatchItem()
    #     container = response.xpath('//div[@class="product-info-main"]')
    #     # naming = container.xpath('.//h1[@class="product-info-naming-description ow-font-bold"]')
        
    #     # item['watch_url'] = response.url
    #     item['collection'] = container.xpath('//.h1//span[@class="product attribute collection hidden"]/text()').get()
    #     yield item
         
    # def parse_each_watch(self, response):
    #        yield{
    #            'watch': response
    #        }
    
    '''
  
    # def start_requests(self):
    #     yield scrapy.Request(
    #         url = "https://www.omegawatches.com/en-us/watchfinder?p=72",
    #         headers={
    #             'Referer': 'https://www.omegawatches.com/en-us/watchfinder?p=71'
    #         }
    #     )
 
        # request = SeleniumRequest(
        #     url=start_url, 
        #     callback=self.load_all_watches,
        # )
        # yield request
        
        
        # driver = response.meta['driver']
        # actions = ActionChains(driver)
        # previous_url = response.url
        # loader_element = driver.find_element(By.XPATH, '//a[@class="action next"]')
        # # element = driver.find_element(By.CSS_SELECTOR,'div.product-list-pager')
    
        # element_selector = "#product-list-toolbar-top > div > div > a"
        # # Check if the element is visible on the page using JavaScript
        # def is_element_present(selector):
        #     return driver.execute_script(
        #         f"return document.querySelector('{selector}') !== null && document.querySelector('{selector}').offsetParent !== null;"
        #     )
        #     #product-list-toolbar-top > div > div > a
        # # Function to scroll the page until the element is visible
        # def scroll_until_element_visible(selector):
        #     while not is_element_present(selector):
        #         driver.execute_script(f"document.getElementById('{selector}').scrollIntoView(true);")
                
        # # Scroll the page until the element is visible
        # scroll_until_element_visible(loader_element)
        
        # while True:
        #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #     # scroll_until_element_visible(loader_element)            # scroll_until_element_visible(element_selector)
        #     WebDriverWait(driver,10).until(EC.url_changes(previous_url))
           
        #     current_url = driver.current_url
        #     if current_url == previous_url:
        #         break
        #     else: 
        #         previous_url = current_url
            