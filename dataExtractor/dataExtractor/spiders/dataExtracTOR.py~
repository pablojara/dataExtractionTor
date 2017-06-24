# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from urlparse import urlparse
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils.url import urljoin_rfc
from dataExtractor.items import torItem
import pdb


class Spider(CrawlSpider):


    name = "dataExtractor"

    # All the http_sttus are handled in this spider
    handle_httpstatus_list = [300, 301, 302, 303, 304, 305, 306, 307, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 500, 501, 502, 503, 504, 505]
    # Extracted items counter
    m = 0
    
    

    # Seed links to start the crawler:  http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page || http://wiki5kauuihowqi5.onion/  -->  The crawler is executed one time for each of this urls
    start_urls = ["http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page"]


    # Simple spider with simple rule, extract and follow all the links found in each page
    rules = [
        Rule(
            LinkExtractor(allow=('https?:\/\/[^\/]*\.onion\/'),
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items",
        )
    ]

    # Method to start extracting pages
    def start_requests(self):

        for url in self.start_urls:
	    pdb.set_trace()
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # Method for parsing the extracted items
    def parse_items(self, response):
	

	hxs = HtmlXPathSelector(response)
        i = torItem()

        i['url'] = response.url
        i['http_status'] = response.status
        llinks=[]

    # Extracting all the links for each page
	for anchor in hxs.select('//a[@href]'):
	    href=anchor.select('@href').extract()[0]
	    if not href.lower().startswith("javascript"):
		llinks.append(urljoin_rfc(response.url,href))
		i['linkedurls'] = llinks
	
	print "#", self.m, " STATUS:", response.status, " URL:", response.url
	self.m = self.m + 1      
	return i


