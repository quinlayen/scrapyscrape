# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WatchItem(scrapy.Item):
    watch_url = scrapy.Field()
    img_url = scrapy.Field()
    watch_price = scrapy.Field()
    # url = scrapy.Field()
    # url = scrapy.Field()
    # url = scrapy.Field()
    # url = scrapy.Field()
    # url = scrapy.Field()
    # url = scrapy.Field()

