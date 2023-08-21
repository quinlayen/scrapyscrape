
# from scrapfly import ScrapeConfig
# from scrapfly.scrapy import ScrapflyMiddleware, ScrapflyScrapyRequest, ScrapflySpider, ScrapflyScrapyResponse
from ..items import WatchItem
from ..itemloaders import OmegaItemLoader
import scrapy
from scrapy.loader import ItemLoader
from scrapy import Selector
import os
import json
from w3lib.html import remove_tags
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from scrapy.selector import HtmlXPathSelector
# from scrapy.http import HtmlResponse
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('SCRAPFLY_API_KEY')


class OmegaSpider(CrawlSpider):
    name = "omega"
    allowed_domains = ["omegawatches.com"]
    start_urls = ["https://www.omegawatches.com/en-us/watchfinder?p=5"]
    # start_urls = ["https://www.omegawatches.com/en-us/watchfinder?filter_movement_type=Q"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//ol[@class="products list items product-items"]//a')), callback="parse_item"),
    )
    
    def parse_item(self, response):
        loader = OmegaItemLoader(item=WatchItem(), response=response)

        
        features_li_tags = response.xpath('//div[@class="product-info-data-content features watches"]/ul/li')
        # for feature_text in features_li_tags.xpath('.//span/text()').extract()
       
 
        if 'quartz' in response.url:
            # battery_life_xpath = '//div[@class="product-info-data-content movement watches"]//li[3]/span/text()'
            caliber_xpath = '//div[@class="product-info-data-content movement watches"]//li[1]/span/text()'
            movement_xpath = '//div[@class="product-info-data-content movement watches"]//li[4]/span/text()'
        else:
            # power_reserve_xpath = 'normalize-space(//ul[@class="ow-mod_37__pictos"]/li[1]/span/text())'
            caliber_xpath = '//div[@class="ow-mod__col-content"]/h2/span[@class="pm-title"]/span[2]/text()'
            movement_xpath = 'normalize-space(//ul[@class="ow-mod_37__pictos"]/li[2]/span/text())'
            # frequency_xpath = 'normalize-space(//ul[@class="ow-mod_37__pictos"]/li[3]/span/text())'
   
        #####   
        for li_tag in features_li_tags:
            features_text = li_tag.xpath('.//span/text()').get()
            
            loader.add_value('features', features_text)
            
        loader.add_value('brand', 'Omega')
        loader.add_value('style', ' ')
        loader.add_value('year_introduced', ' ')
        loader.add_value('case_finish', ' ')
        loader.add_xpath('caseback', '//*[@id="product-info-description"]/div/div/p/text()')
        loader.add_xpath('bezel_material', '//*[@id="product-info-description"]/div/div/p/text()')
        loader.add_value('bezel_color', ' ')
        loader.add_xpath('numerals', '//*[@id="product-info-description"]/div/div/p/text()')
        loader.add_xpath('bracelet_color', '//*[@id="tab-strap"]/ul/li[2]/span/text()')
        loader.add_value('jewels', ' ')
        loader.add_value('year_introduced', ' ')
        loader.add_xpath('numerals', '//*[@id="product-info-description"]/div/div/p/text()')
        loader.add_xpath('bracelet_color', '//*[@id="tab-strap"]/ul/li[2]/span/text()')
        loader.add_xpath('marketing_name', '//span[contains (@class, "product attribute marketing-name")]/text()')
        loader.add_value('watch_url', response.url)
        loader.add_xpath('parent_model','//span[@class="product attribute collection hidden"]/text()')
        loader.add_xpath('specific_model','//span[@class="product attribute subcollection"]/text()')
        loader.add_xpath('nickname','//span[@class="product attribute name"]/text()')
        loader.add_xpath('sku','//p[@class="product attribute sku"]/span/text()')
        loader.add_xpath('description','//*[@id="product-info-description"]/div/div/p/text()')
        loader.add_value('currency','USD')
        loader.add_xpath('price','//span[@class="price"]/text()')
        loader.add_xpath('case_material','//span[@data-code="watch_watchcase"]/text()')
        loader.add_xpath('case_diameter','//span[@data-code="watch_casediameter"]/text()')
        loader.add_xpath('between_lugs','//span[@data-code="watch_between_lugs_size"]/text()')
        loader.add_xpath('case_thickness','//span[@data-code="watch_thickness"]/text()')
        loader.add_xpath('lug_to_lug','//span[@data-code="watch_lug_to_lug"]/text()')
        loader.add_xpath('weight','//span[@data-code="weight"]/text()')
        loader.add_xpath('water_resistance','//span[@data-code="watch_waterresistance"]/text()')
        loader.add_xpath('crystal','//span[@data-code="watch_crystal"]/text()')
        loader.add_xpath('bracelet_material','//span[@data-code="watch_bracelet"]/text()')
        loader.add_xpath('clasp_type','//span[@data-code="strap_clasp_type"]/text()')
        loader.add_xpath('frequency', 'normalize-space(//ul[@class="ow-mod_37__pictos"]/li[3]/span/text())')
        loader.add_xpath('movement', movement_xpath)
        loader.add_xpath('caliber', caliber_xpath)
        loader.add_xpath('power_reserve', 'normalize-space(//ul[@class="ow-mod_37__pictos"]/li[1]/span/text())')
        loader.add_xpath('battery_life', '//div[@class="product-info-data-content movement watches"]//li[3]/span/text()')
        loader.add_xpath('dial_color','//span[@data-code="watch_dial" ]/text()')
        # loader.add_xpath('image_urls','//*[@id="gallery-frame-0"]/img[2]/@src')
        yield loader.load_item()

      
 


        
           
        
        
# class OmegaSpider(scrapy.Spider):
        
        
#     name = "omega"
#     allowed_domains = ["omegawatches.com"]
#     start_urls = ["https://www.omegawatches.com/en-us/watchfinder?p=72"]
    
  
    
    # def parse_img_urls(self, images):
    #     image_list = images.split(" ")
    #     return image_list[-2]
        
    # def parse(self, response):
    #     link_extractor = LinkExtractor()
    #     item = WatchItem()
    #     # extracting links (returns List of links)
    #     links = link_extractor.extract_links(response)
    #     for link in link_extractor.extract_links(response):
    #         yield scrapy.Request(link.url, callback=self.parse_watches)
            
    #     watch_container = response.xpath('//li[@class="product-item"]')
    #     for watch in watch_container:
    #         item['watch_url'] = watch.xpath('.//a[@class="ow-prod__img"]/@href').get(),
    #         # item['image_urls'] = self.parse_img_urls(watch.xpath('.//a[@class="ow-prod__img"]/picture/source/@data-srcset').get()),
    #         item['price'] = watch.xpath('.//span[@class="price"]/text()').get()     
    #         yield item
  
         
      
    # def pars_watches(self,response):
    #     print(response)
  
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
