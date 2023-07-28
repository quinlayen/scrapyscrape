# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WatchItem(scrapy.Item):
    watch_url = scrapy.Field()
    parent_model = scrapy.Field()
    specific_model = scrapy.Field()
    nickname = scrapy.Field()
    sku = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    case_material = scrapy.Field()
    case_diameter = scrapy.Field()
    between_lugs = scrapy.Field()
    case_thickness = scrapy.Field()
    lug_to_lug = scrapy.Field()
    weight = scrapy.Field()
    water_resistance = scrapy.Field()
    crystal = scrapy.Field()
    clasp_material = scrapy.Field()
    clasp_type = scrapy.Field()
    # image_urls = scrapy.Field()
    # images = scrapy.Field()

