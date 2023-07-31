# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity
import re


def extract_crystal(input_string):
    pattern = r'\bsapphire\b'
    
    match = re.search(pattern, input_string)
    if match:
        return match.group(0)
    else:
        return None
    
def clean_caliber(caliber):
    return caliber[-4:]
    
def clean_power_reserve(power):
    split_list = power.split(' ')
    return split_list[0]

# def get_all_features(xpath):
#     for feature in xpath
# 
def parse_img_urls(images):
    image_list = images.split(" ")
    return image_list[-2]

def clean_features(feature_list):
    return [feature.strip() for feature in feature_list.split(',')]
    
   
class WatchItem(scrapy.Item):
    watch_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    parent_model = scrapy.Field(
        output_processor = TakeFirst()
    )
    specific_model = scrapy.Field(
        output_processor = TakeFirst()
    )
    nickname = scrapy.Field(
        output_processor = TakeFirst()
    )
    sku = scrapy.Field(
        output_processor = TakeFirst()
    )
    description = scrapy.Field(
        output_processor = Join('')
    )
    price = scrapy.Field(
        output_processor = TakeFirst()
    )
    case_material = scrapy.Field(
        output_processor = TakeFirst()
    )
    case_diameter = scrapy.Field(
        output_processor = TakeFirst()
    )
    between_lugs = scrapy.Field(
        output_processor = TakeFirst()
    )
    case_thickness = scrapy.Field(
        output_processor = TakeFirst()
    )
    lug_to_lug = scrapy.Field(
        output_processor = TakeFirst()
    )
    weight = scrapy.Field(
        output_processor = TakeFirst()
    )
    water_resistance = scrapy.Field(
        output_processor = TakeFirst()
    )
    crystal = scrapy.Field(
        input_processor = MapCompose(extract_crystal),
        output_processor = TakeFirst()
    )
    bracelet_material = scrapy.Field(
        output_processor = TakeFirst()
    )
    clasp_type = scrapy.Field(
        output_processor = TakeFirst()
    )
    dial_color = scrapy.Field(
        output_processor = TakeFirst()
    )
    power_reserve = scrapy.Field(
        input_processor = MapCompose(clean_power_reserve),
        output_processor = TakeFirst()
    )
    battery_life = scrapy.Field(
        output_processor = TakeFirst()
    )
    caliber = scrapy.Field(
        input_processor = MapCompose(clean_caliber),
        output_processor = TakeFirst()
    )
    features = scrapy.Field(
        input_processor = MapCompose(clean_features),
        output_processor = Join(' , ')
    )
    # image_urls = scrapy.Field()
    # images = scrapy.Field()

