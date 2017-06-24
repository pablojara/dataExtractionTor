# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy
from scrapy.item import Item, Field


class torItem(Item):
     url=Field()
     http_status=Field()
     linkedurls=Field()
     referer=Field()

