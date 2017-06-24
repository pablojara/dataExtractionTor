# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import os
import random
from scrapy.conf import settings
import urlparse
from collections import defaultdict
from scrapy.exceptions import IgnoreRequest





class DataextractorSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    # Middleware used to change the UserAgent for each request

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)

    # Middleware used to connect the crawler with the proxy server Polipo

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')


    # Middleware used to limit the number of extracted pages per domain to 2.000

class FilterDomainbyLimitMiddleware(object):
    def __init__(self, domains_to_filter):
        self.domains_to_filter = domains_to_filter
        self.counter = defaultdict(int)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        spider_name = crawler.spider.name
        domains_to_filter = settings.get('DOMAINS_TO_FILTER')
        o = cls(domains_to_filter)
        return o
    
    def process_request(self, request, spider):
        parsed_url = urlparse.urlparse(request.url)
	if (self.counter.get(parsed_url.netloc, 0) < 2000):
            self.counter[parsed_url.netloc] += 1
        else:
	    raise IgnoreRequest()

