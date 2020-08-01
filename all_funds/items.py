# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AllFundsItem(scrapy.Item):
    # define the fields for your item here like:

    code = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    networth = scrapy.Field()
    current_value = scrapy.Field()
    change_percent = scrapy.Field()


    pass
