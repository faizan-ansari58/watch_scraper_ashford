import scrapy
from scrapy.loader import ItemLoader
from watch_scraper.items import WatchScraperItem
import re

class WatchSpider(scrapy.Spider):
    name = 'women_watch_spider'
    start_urls = ['https://www.ashford.com/womens-watches.html']
    def clean_text(text):
        # Remove non-breaking space (\xa0) and other unwanted characters
        cleaned_text = re.sub(r'\xa0', ' ', text)
        cleaned_text = cleaned_text.strip()
        # Add more cleaning logic if needed
        return cleaned_text
    def parse(self, response):
        watch_brands_soup = response.css('form#am-ranges-brand ol li')
        for brand in watch_brands_soup:
            brand_name = brand.css('span.label::text').get()
            count_text = brand.css('span.count::text').get().strip()
            watch_count = int(re.search(r'\d+', count_text).group())
            total_pages = (watch_count + 79) // 80

            for page_num in range(1, total_pages + 1):
                url = f'https://www.ashford.com/womens-watches.html?brand={brand_name}&p={page_num}'
                yield scrapy.Request(url, callback=self.parse_watch_list, meta={'brand_name': brand_name})

    def parse_watch_list(self, response):
        brand_name = response.meta['brand_name']
        links = response.css('strong.product.name.product-item-name a')

        for link in links:
            href = link.attrib['href']
            yield scrapy.Request(href, callback=self.parse_watch, meta={'brand_name': brand_name})

    def parse_watch(self, response):
        loader = ItemLoader(item=WatchScraperItem(), response=response)
        loader.add_value('link', response.url)
        loader.add_css('image', 'img.gallery-placeholder__image::attr(src)')
        loader.add_css('name', 'span.f-17.qvPrdURL.product-url-text.text-capitalize::text')
        loader.add_css('old_price', 'span.old-price span.price::text')
        loader.add_css('discounted_price', 'span.special-price span.price::text')
        loader.add_css('brand', 'span[data-th="Brand Name"] a::text')
        loader.add_css('sku', 'span[data-th="SKU"]::text')
        loader.add_css('collection', 'span[data-th="Collection"] a::text')
        loader.add_css('country_of_manufacture', 'span[data-th="Country of Manufacture"]::text')
        loader.add_css('model_alias', 'span[data-th="Model Alias"]::text')
        loader.add_css('upc', 'span[data-th="UPC"]::text')
        loader.add_css('features', 'span[data-th="Feature"]::text')
        loader.add_css('movement_type', 'span[data-th="Type"]::text')
        loader.add_css('movement_jewels', 'span[data-th="Jewels"]::text')
        loader.add_css('movement_caliber', 'span[data-th="Caliber"]::text')
        loader.add_css('movement_calendar', 'span[data-th="Calendar"]::text')
        loader.add_css('movement_crown', 'span[data-th="Crown"]::text')
        loader.add_css('movement_power_reserve', 'span[data-th="Power Reserve"]::text')
        loader.add_css('dial_color', 'span[data-th="Dial Color"] a::text')
        loader.add_css('case_width', 'span[data-th="Case Width"]::text')
        loader.add_css('case_depth', 'span[data-th="Case Depth"]::text')
        loader.add_css('case_back', 'span[data-th="Case Back"]::text')
        loader.add_css('case_crystal', 'span[data-th="Crystal"]::text')
        loader.add_css('case_material', 'span[data-th="Material"]::text')
        loader.add_css('case_shape', 'span[data-th="Shape"]::text')
        loader.add_css('water_resistance', 'span[data-th="Water Resistance"]::text')
        loader.add_css('band_color', 'span[data-th="Band Color"]::text')
        loader.add_css('band_material', 'span[data-th="Band Material"]::text')
        loader.add_css('band_type', 'span[data-th="Band Type"] a::text')
        loader.add_css('band_length', 'span[data-th="Band Length"]::text')
        loader.add_css('band_width', 'span[data-th="Band Width"]::text')
        loader.add_css('band_clasp', 'span[data-th="Clasp"]::text')

        yield loader.load_item()
