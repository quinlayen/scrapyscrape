

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
    
    def clean_water_resistance(input_string):
        cleaned_string = input_string.split(' ')[0]
        return cleaned_string + ' ATM'
    
    def search_numerals_substring(description):
        if 'Roman' in description:
            return 'Roman numerals'
        elif 'Arabic' in description:
            return 'Arabic numerals'
        else:
            return 'No numerals'
        
    # TODO: parse caseback in features    
    def parse_caseback(description):
        pattern = r'(\w+\s+\w+)\s+' + re.escape('caseback')
      
        match = re.search(pattern, description)
        
        if match:
            words_before = match.group(1)
            allowed_caseback = ['stainless steel', 'transparent', 'sapphire crystal']
            if words_before in allowed_caseback:
                return words_before
            else:
                return None
        else:
            return None
    
    def parse_bezel_material(description):
        pattern = r'(\w+\s+\w+)\s+' + re.escape('bezel')
    
        match = re.search(pattern, description)
        
        if match:
            words_before = match.group(1)
            allowed_bezel = ['stainless steel', 'aluminium', 'ceramic']
            if words_before in allowed_bezel:
                return words_before
            else:
                return None
        else:
            return None
    
    default_output_processor = TakeFirst()
    
    caliber_in = MapCompose(lambda x : x[-4:])
    
    price_in = MapCompose(lambda x: x.split('$')[-1])
    
    power_reserve_in = MapCompose(lambda x : x.split(' ')[0:2])
    power_reserve_out = Join(' ')
    
    description_out = Join()
    
    crystal_in = MapCompose(extract_crystal)
    
    features_in = MapCompose(clean_features)
    features_out = Identity()

    
    water_resistance_in = MapCompose(clean_water_resistance)
   
    numerals_in = MapCompose(search_numerals_substring)
    
    caseback_in = MapCompose(parse_caseback)
    
    bezel_material_in = MapCompose(parse_bezel_material)
    
    # image_urls_in = MapCompose(lambda x : x.split(" ")[-2])