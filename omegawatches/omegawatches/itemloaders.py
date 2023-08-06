

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity
import re

class OmegaItemLoader(ItemLoader):
    
    def extract_crystal(input_string):
        pattern = r'\bsapphire\b'
        
        match = re.search(pattern, input_string)
        if match:
            return match.group(0)
        else:
            return None
        
    def clean_features(feature_list):
        return [feature.strip() for feature in feature_list.split(',')]
    
    default_output_processor = TakeFirst()
    
    caliber_in = MapCompose(lambda x : x[-4:])
    
    power_reserve_in = MapCompose(lambda x : x.split(' ')[0:2])
    power_reserve_out = Join(' ')
    
    description_out = Join()
    
    crystal_in = MapCompose(extract_crystal)
    
    features_in = MapCompose(clean_features)
    features_out = Join(' , ')
    
    # image_urls_in = MapCompose(lambda x : x.split(" ")[-2])