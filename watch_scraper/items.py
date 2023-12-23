import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
import re

def clean_text(text):
    # Remove non-breaking space (\xa0) and other unwanted characters
    cleaned_text = re.sub(r'\xa0', ' ', text)
    cleaned_text = cleaned_text.strip()
    # Add more cleaning logic if needed
    return cleaned_text

class WatchScraperItem(scrapy.Item):
    link = scrapy.Field()
    image = scrapy.Field()
    name = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip(), clean_text),
        output_processor=TakeFirst()
    )
    old_price = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    discounted_price = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    brand = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    sku = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    collection = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    country_of_manufacture = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    model_alias = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    upc = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    features = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    movement_type = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    movement_jewels = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    movement_caliber = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    movement_calendar = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    movement_crown = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    movement_power_reserve = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    dial_color = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    case_width = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    case_depth = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    case_back = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    case_crystal = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    case_material = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    case_shape = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    water_resistance = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    band_color = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    band_material = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    band_type = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    band_length = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    band_width = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    band_clasp = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
