# -*- coding: utf-8 -*-

# Scrapy settings for dataExtractor project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dataExtractor'

SPIDER_MODULES = ['dataExtractor.spiders']
NEWSPIDER_MODULE = 'dataExtractor.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'test1 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 200

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:

#CONCURRENT_ITEMS = 1
#CONCURRENT_REQUESTS_PER_DOMAIN = 1
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

RETRY_ENABLED = True

DOWNLOAD_FAIL_ON_DATALOSS = False

HTTPCACHE_IGNORE_MISSING = True

#HTTPERROR_ALLOW_ALL = True

LOG_ENABLED = True

LOG_LEVEL = 'CRITICAL'

DOWNLOAD_TIMEOUT = 20

AJAXCRAWL_ENABLED = True

REDIRECT_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


EXTENSIONS = {
    "scrapy_graph_export.ScrapyGraphExport": 1000
}

EXPORTER_OUTPUT_DIRECTORY = "/tmp"

DOMAINS_TO_FILTER = {

}

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'test1.middlewares.Test1SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
     'dataExtractor.middlewares.RandomUserAgentMiddleware': 400,
     'dataExtractor.middlewares.ProxyMiddleware': 410,
     'dataExtractor.middlewares.FilterDomainbyLimitMiddleware':100,
     'dataExtractor.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None
    # Disable compression middleware, so the actual HTML pages are cached
}
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'test1.pipelines.Test1Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True

# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings

#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT_LIST = [
    """Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 
         (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7""",
    """Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) 
       Gecko/16.0 Firefox/16.0""",
    """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 
       (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10"""
]
HTTP_PROXY = 'http://127.0.0.1:8123'
