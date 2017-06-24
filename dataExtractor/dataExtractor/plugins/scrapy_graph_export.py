from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.conf import settings
import os
import os.path
from dataExtractor.items import torItem
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
import json
from scrapy.exporters import JsonLinesItemExporter
from scrapy.utils.serialize import ScrapyJSONEncoder
from scrapy.exporters import JsonItemExporter


    #Plugin for processing all the extracted items and export them to a JSON file

class ScrapyGraphExport(object):

    #Open the exporting file and init the spider
    def __init__(self):
        dispatcher.connect(self.response_received, signal=signals.response_received)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)
        dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        self.output = {}
	self.file = open("/tmp/rawData_1.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
    def spider_opened(self,spider):
	print "Spider opened"

    def response_received(self, response, request, spider):

	hxs = HtmlXPathSelector(response)
        i = torItem()
        i['url'] = response.url
        i['http_status'] = response.status
        llinks=[]
	for anchor in hxs.select('//a[@href]'):
	    href=anchor.select('@href').extract()[0]
	    if not href.lower().startswith("javascript"):
		llinks.append(urljoin_rfc(response.url,href))
		i['linkedurls'] = llinks
        if request.headers.has_key('Referer'):
	   i['referer'] = request.headers['Referer']
	   self.exporter.export_item(i)
           return i

    def spider_closed(self,spider):
        self.file.close()


