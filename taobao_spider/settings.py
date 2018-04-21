# -*- coding: utf-8 -*-

# Scrapy settings for taobao_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao_spider'

SPIDER_MODULES = ['taobao_spider.spiders']
NEWSPIDER_MODULE = 'taobao_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'  # 设置用户代理值

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 不遵循 robots.txt协议

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    # 'Connection': 'keep-alive',
    # 'Host': 'www.taobao.com',
    'Referer': 'https://www.taobao.com/',
    # 'upgrade-insecure-requests': '1',
    # 'cache-control':'max-age=0'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'taobao_spider.middlewares.JavaScriptMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'taobao_spider.middlewares.JavaScriptMiddleware': 500,   # 键为中间件类的路径，值为中间件的顺序
#     'taobao_spider.middlewares.RandomUserAgent': 500
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'taobao_spider.pipelines.TaobaoSpiderPipeline': 1,
    'taobao_spider.pipelines.ImagesPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# SCHEDULER = "scrapy_redis.scheduler.Scheduler"  #启用Redis调度存储请求队列
# SCHEDULER_PERSIST = True    #不清除Redis队列、这样可以暂停/恢复 爬取
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #确保所有的爬虫通过Redis去重
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# REDIS_HOST = '127.0.0.1'  # 也可以根据情况改成 localhost
# REDIS_PORT = 6379

USER_AGENT_LIST = [
    #    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    #    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# USER_AGENT_LIST = ['zspider/0.9-dev http://feedback.redkolibri.com/',
#                     'Xaldon_WebSpider/2.0.b1',
#                     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
#                     'Mozilla/5.0 (compatible; Speedy Spider; http://www.entireweb.com/about/search_tech/speedy_spider/)',
#                     'Speedy Spider (Entireweb; Beta/1.3; http://www.entireweb.com/about/search_tech/speedyspider/)',
#                     'Speedy Spider (Entireweb; Beta/1.2; http://www.entireweb.com/about/search_tech/speedyspider/)',
#                     'Speedy Spider (Entireweb; Beta/1.1; http://www.entireweb.com/about/search_tech/speedyspider/)',
#                     'Speedy Spider (Entireweb; Beta/1.0; http://www.entireweb.com/about/search_tech/speedyspider/)',
#                     'Speedy Spider (Beta/1.0; www.entireweb.com)',
#                     'Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
#                     'Speedy Spider (http://www.entireweb.com/about/search_tech/speedyspider/)',
#                     'Speedy Spider (http://www.entireweb.com)',
#                     'Sosospider+(+http://help.soso.com/webspider.htm)',
#                     'sogou spider',
#                     'Nusearch Spider (www.nusearch.com)',
#                     'nuSearch Spider (compatible; MSIE 4.01; Windows NT)',
#                     'lmspider (lmspider@scansoft.com)',
#                     'lmspider lmspider@scansoft.com',
#                     'ldspider (http://code.google.com/p/ldspider/wiki/Robots)',
#                     'iaskspider/2.0(+http://iask.com/help/help_index.html)',
#                     'iaskspider',
#                     'hl_ftien_spider_v1.1',
#                     'hl_ftien_spider',
#                     'FyberSpider (+http://www.fybersearch.com/fyberspider.php)',
#                     'FyberSpider',
#                     'everyfeed-spider/2.0 (http://www.everyfeed.com)',
#                     'envolk[ITS]spider/1.6 (+http://www.envolk.com/envolkspider.html)',
#                     'envolk[ITS]spider/1.6 ( http://www.envolk.com/envolkspider.html)',
#                     'Baiduspider+(+http://www.baidu.com/search/spider_jp.html)',
#                     'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
#                     'BaiDuSpider',
#                     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com',
#                    ]

DOWNLOADER_MIDDLEWARES = {
    'taobao_spider.MidWare.HeaderMidWare.ProcessHeaderMidware': 543,
    'taobao_spider.middlewares.JavaScriptMiddleware': 500,  # 键为中间件类的路径，值为中间件的顺序
    'taobao_spider.middlewares.ProxyMiddleware': 490,
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    # 'scrapy_proxies.RandomProxy': 100,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# scrapy-proxies配置，参考：https://github.com/aivarsk/scrapy-proxies
# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = 'D:\\svn\\shenhui\\taobao_spider\\taobao_spider\\proxy_list.txt'

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
# CUSTOM_PROXY = "http://host1:port"

IMAGES_STORE = "D:/pic/"
PHANTOMJS_PATH = "D:\\work\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"
# PROXIES = [
#     'http://119.128.172.105:8118',
#     'http://218.72.109.70:18118',
#     'http://218.72.109.166:18118',
#     'http://183.159.90.136:18118',
#     'http://183.159.92.0:18118',
#     'http://111.155.116.237:8123',
#     'http://49.79.193.138:61234',
#     'http://114.215.83.184:3128',
#     'http://122.114.31.177:808',
#     'http://61.135.217.7:80',
#     'http://183.159.93.159:18118',
#     'http://60.177.227.108:18118',
#     'http://123.56.89.238:60443',
#     'http://42.7.26.21:60443',
#     'http://183.159.94.22:18118',
#     'http://183.159.91.212:18118',
#     'http://27.217.155.8:8118',
#     'http://111.192.176.169:8118',
#     'http://183.159.95.16:18118',
#     'http://60.177.228.169:18118'
# ]

PROXIES = [
    {'ip_port': '119.128.172.105:8118', 'user_pass': ''},
    {'ip_port': '218.72.109.70:18118', 'user_pass': ''},
    {'ip_port': '218.72.109.166:18118', 'user_pass': ''},
    {'ip_port': '183.159.90.136:18118', 'user_pass': ''},
    {'ip_port': '183.159.92.0:18118', 'user_pass': ''},
    {'ip_port': '111.155.116.237:8123', 'user_pass': ''},
    {'ip_port': '49.79.193.138:61234', 'user_pass': ''},
    {'ip_port': '114.215.83.184:3128', 'user_pass': ''},
    {'ip_port': '122.114.31.177:808', 'user_pass': ''},
    {'ip_port': '61.135.217.7:80', 'user_pass': ''},
    {'ip_port': '183.159.93.159:18118', 'user_pass': ''},
    {'ip_port': '60.177.227.108:18118', 'user_pass': ''},
    {'ip_port': '123.56.89.238:60443', 'user_pass': ''},
    {'ip_port': '42.7.26.21:60443', 'user_pass': ''},
    {'ip_port': '183.159.94.22:18118', 'user_pass': ''},
    {'ip_port': '183.159.91.212:18118', 'user_pass': ''},
    {'ip_port': '27.217.155.8:8118', 'user_pass': ''},
    {'ip_port': '111.192.176.169:8118', 'user_pass': ''},
    {'ip_port': '183.159.95.16:18118', 'user_pass': ''},
    {'ip_port': '60.177.228.169:18118', 'user_pass': ''},
]

# MONGO_HOST = "127.0.0.1"  # 主机IP
# MONGO_PORT = 27017  # 端口号
# MONGO_DB = "tbdb"  # 库名
# MONGO_COLL = "taobao"  # collection名
# MONGO_USER = "username"
# MONGO_PSW = "password"
