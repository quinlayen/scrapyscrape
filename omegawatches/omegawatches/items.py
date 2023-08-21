# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

    
   
class WatchItem(scrapy.Item):

    brand = scrapy.Field()
    style = scrapy.Field()
    year_introduced = scrapy.Field()
    case_finish = scrapy.Field()
    caseback = scrapy.Field()
    bezel_material = scrapy.Field()
    bezel_color = scrapy.Field()
    numerals = scrapy.Field()
    bracelet_color = scrapy.Field()
    movement = scrapy.Field()
    frequency = scrapy.Field()
    jewels = scrapy.Field()
    watch_url = scrapy.Field()
    parent_model = scrapy.Field()
    specific_model = scrapy.Field()
    nickname = scrapy.Field()
    marketing_name = scrapy.Field()
    sku = scrapy.Field()
    description = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    case_material = scrapy.Field()
    case_diameter = scrapy.Field()
    between_lugs = scrapy.Field()
    case_thickness = scrapy.Field()
    lug_to_lug = scrapy.Field()
    weight = scrapy.Field()
    water_resistance = scrapy.Field()
    crystal = scrapy.Field()
    bracelet_material = scrapy.Field()
    clasp_type = scrapy.Field()
    dial_color = scrapy.Field()
    power_reserve = scrapy.Field()
    battery_life = scrapy.Field()
    caliber = scrapy.Field()
    features = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    
    
    # from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity
# import re


# def extract_crystal(input_string):
#     pattern = r'\bsapphire\b'
    
#     match = re.search(pattern, input_string)
#     if match:
#         return match.group(0)
#     else:
#         return None
    
# def clean_caliber(caliber):
#     return caliber[-4:]
    
# def clean_power_reserve(power):
#     split_list = power.split(' ')
#     return power.split(' ')[0:2]

# def parse_img_urls(images):
#     image_list = images.split(" ")
#     return image_list[-2]

# def clean_features(feature_list):
#     return [feature.strip() for feature in feature_list.split(',')]
    
# class WatchItem(scrapy.Item):
    
#     watch_url = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     parent_model = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     specific_model = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     nickname = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     sku = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     description = scrapy.Field(
#         output_processor = Join('')
#     )
#     price = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     case_material = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     case_diameter = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     between_lugs = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     case_thickness = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     lug_to_lug = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     weight = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     water_resistance = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     crystal = scrapy.Field(
#         input_processor = MapCompose(extract_crystal),
#         output_processor = TakeFirst()
#     )
#     bracelet_material = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     clasp_type = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     dial_color = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     power_reserve = scrapy.Field(
#         input_processor = MapCompose(clean_power_reserve),
#         output_processor = Join(' ')
#     )
#     battery_life = scrapy.Field(
#         output_processor = TakeFirst()
#     )
#     caliber = scrapy.Field(
#         input_processor = MapCompose(clean_caliber),
#         output_processor = TakeFirst()
#     )
#     features = scrapy.Field(
#         input_processor = MapCompose(clean_features),
#         output_processor = Join(' , ')
#     )
    # image_urls = scrapy.Field()
    # images = scrapy.Field()

