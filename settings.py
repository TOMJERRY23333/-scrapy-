# -*- coding: utf-8 -*-

# Scrapy settings for weibouser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibouser'  #Scrapy项目实现的bot的名字(也为项目名称)

SPIDER_MODULES = ['spiders'] # Scrapy搜索spider的模块列表。
NEWSPIDER_MODULE = 'spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 爬取的默认User-Agent，除非被覆盖。
#USER_AGENT = 'weibouser (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 如果启用，Scrapy将会尊重 robots.txt策略。
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# Scrapy downloader 并发请求(concurrent requests)的最大值
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度，
# 减轻服务器压力。同时也支持小数:0.25    # 250 ms of delay
# 另外您可以通过spider的 download_delay 属性为每个spider设置该设定。
DOWNLOAD_DELAY = 2

# 下载器超时时间(单位: 秒)。
# 该超时值可以使用 download_timeout 来对每个spider进行设置, 也可以使用 download_timeout Request.meta key 来对每个请求进行设置.
# DOWNLOAD_TIMEOUT=180

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN 对单个网站进行并发请求的最大值。
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 对单个IP进行并发请求的最大值。如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定，
# 使用该设定。 也就是说，并发限制将针对IP，而不是网站。
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 否启用cookies middleware。如果关闭，cookies将不会发送给web server。
# COOKIES_ENABLED = False
# 如果启用，Scrapy将记录所有在request(Cookie 请求头)发送的cookies及response接收到的cookies(Set-Cookie 接收头)。
# COOKIES_DEBUG = False


# Disable Telnet Console (enabled by default)
# 表明 telnet 终端 (及其插件)是否启用的布尔值。
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:（下载中间件之一：默认请求头中间件）
# ‘’‘Scrapy HTTP Request使用的默认header。DEFAULT_REQUEST_HEADERS由 DefaultHeadersMiddleware 指定。’‘’
# DEFAULT_REQUEST_HEADERS = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
#         'cookie': 'SINAGLOBAL=3762728309341.974.1643475551958; UOR=,,www.baidu.com; SSOLoginState=1658043697; _s_tentry=-; Apache=5024335155565.665.1658147584064; ULV=1658147584257:17:1:1:5024335155565.665.1658147584064:1653833382856; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Il4DJWM_fxzm436ObB32s5JpX5KMhUgL.FoqfS024SK.4eon2dJLoI7RLxK-LBo5L129NqPxoI5tt; ALF=1689845731; SCF=AtVpMW-LtWR0vAUqymFpu7kORb1pwSXmc_OUidT2uk9To13TgPc-BDBixwRe1NzN3VWEBWQdLehuzKW0uWE1Z8U.; SUB=_2A25P07w5DeRhGeBL7FMY9SfFyTSIHXVsqKrxrDV8PUNbmtANLUylkW9NRvUjOigcikDf1aD9esFJTsHBUN3j3CJY'}

# FEED_URI='./%(name)s.csv'
# FEED_FORMAT='CSV'
# FEED_EXPORT_ENCODING='utf-8'

# HTTPERROR_ALLOWED_CODES = [302]

ITEM_PIPELINES = {
    'pipelines.WeiboVideoPipline':1

    }

IMAGES_STORE = './storage/data'
FILES_STORE = './storage/data_3'

DOWNLOAD_MAXSIZE = 0
DOWNLOAD_WARNSIZE = 0
DOWNLOAD_TIMEOUT = 300
# IMAGES_EXPERES = 90
# IMAGES_MIN_HEIGHT = 110
# IMAGES_MIN_WIDTH = 110
# 保存项目中默认启用的spider中间件的字典。 永远不要在项目中修改该设定，而是修改 SPIDER_MIDDLEWARES 。
# SPIDER_MIDDLEWARES_BASE={
#     过滤出所有失败(错误)的HTTP response，因此spider不需要处理这些request。
#     处理这些request意味着消耗更多资源，并且使得spider逻辑更为复杂。
#     根据 HTTP标准 ，返回值为200-300之间的值为成功的resonse。
#     如果您想处理在这个范围之外的response，
#     您可以通过 spider的 handle_httpstatus_list 属性
#     或 HTTPERROR_ALLOWED_CODES（忽略该列表中所有非200状态码的response。） 设置来指定spider能处理的response返回值。
#     例：class MySpider(CrawlSpider):
#            handle_httpstatus_list = [404]
#     'scrapy.contrib.spidermiddleware.httperror.HttpErrorMiddleware': 50,
#
#     过滤出所有URL不由该spider负责的Request。
#     该中间件过滤出所有主机名不在spider属性 allowed_domains 的request。
#     如果spider没有定义 allowed_domains 属性，或该属性为空， 则offsite 中间件将会允许所有request。
#     如果request设置了 dont_filter 属性， 即使该request的网站不在允许列表里，则offsite中间件将会允许该request。
#     'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 500,
#
#      根据生成Request的Response的URL来设置Request Referer 字段。
#     'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': 700,
#
#      过滤出URL长度比URLLENGTH_LIMIT的request  （URLLENGTH_LIMIT - 允许爬取URL最长的长度.）
#     'scrapy.contrib.spidermiddleware.urllength.UrlLengthMiddleware': 800,
#
#      DepthMiddleware是一个用于追踪每个Request在被爬取的网站的深度的中间件。
#      其可以用来限制爬取深度的最大深度或类似的事情。
#     'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': 900,
# }
# 保存项目中启用的下载中间件及其顺序的字典
# 该设置是一个字典，键为中间件的路径，值为中间件的顺序(order)。
# SPIDER_MIDDLEWARES = {
#    'weibouser.middlewares.WeibouserSpiderMiddleware': 543, # 要启用spider中间件，您可以将其加入到 SPIDER_MIDDLEWARES 设置中。
# }



# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 保存项目中启用的1、下载中间件（DOWNLOADER_MIDDLEWARES）及2、其顺序的3、字典。
# DOWNLOADER_MIDDLEWARES设置会与Scrapy定义的 DOWNLOADER_MIDDLEWARES_BASE设置合并(但不是覆盖)，
# 而后根据顺序(order)进行排序，最后得到启用中间件的有序列表:
# 第一个中间件是最靠近引擎的，最后一个中间件是最靠近下载器的。
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
}
# 包含Scrapy默认启用的下载中间件的字典。
# DOWNLOADER_MIDDLEWARES_BASE={
#     该中间件过滤所有robots.txt eclusion standard中禁止的request。
#     'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
#
#      该中间件完成某些使用 Basic access authentication (或者叫HTTP认证)的spider生成的请求的认证过程。
#     'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
#
#     该中间件设置 DOWNLOAD_TIMEOUT 或 spider的 download_timeout 属性指定的request下载超时时间.
#     您也可以使用 download_timeout Request.meta key 来对每个请求设置下载超时时间.
#     这种方式在 DownloadTimeoutMiddleware 被关闭时仍然有效.
#     'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
#
#     用于覆盖spider的默认user agent的中间件。要使得spider能覆盖默认的user agent，其 user_agent 属性必须被设置。
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
#
#      该中间件将重试可能由于临时的问题，例如连接超时或者HTTP 500错误导致失败的页面。
#      爬取进程会收集失败的页面并在最后，spider爬取完所有正常(不失败)的页面后重新调度。
#      一旦没有更多需要重试的失败页面，该中间件将会发送一个信号(retry_complete)， 其他插件可以监听该信号。
#      如果 Request.meta 中 dont_retry 设为True， 该request将会被本中间件忽略。
#       RETRY_ENABLED
#       RETRY_TIMES
#       RETRY_HTTP_CODES = 默认[500, 502, 503, 504, 400, 408]
#     'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
#
#     该中间件设置 DEFAULT_REQUEST_HEADERS 指定的默认request header。
#     'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
#
#      该中间件根据meta-refresh html标签处理request重定向。
#     'scrapy.contrib.downloadermiddleware.redirect.MetaRefreshMiddleware': 580,
#
#      该中间件提供了对压缩(gzip, deflate)数据的支持。
#     'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 590,
#
#     该中间件根据response的状态处理重定向的request。
#     通过该中间件的(被重定向的)request的url可以通过 Request.meta 的 redirect_urls 键找到。
#     如果 Request.meta 中 dont_redirect 设置为True ，则该request将会被此中间件忽略。
#     'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
#
#     该中间件使得爬取需要cookie(例如使用session)的网站成为了可能。 其追踪了web server发送的cookie，并在之后的request中发送回去， 就如浏览器所做的那样。
#     'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
#
#     该中间件提供了对request设置HTTP代理的支持。您可以通过在 Request 对象中设置 proxy 元数据来开启代理。
#     类似于Python标准库模块 urllib 及 urllib2 ，其使用了下列环境变量:
#     http_proxy
#     https_proxy
#     no_proxy
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
#
#     'scrapy.contrib.downloadermiddleware.chunked.ChunkedTransferMiddleware': 830,
#
#     保存所有通过的request、response及exception的中间件。您必须启用 DOWNLOADER_STATS 来启用该中间件。
#     'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
#
#     该中间件为所有HTTP request及response提供了底层(low-level)缓存支持。 其由cache存储后端及cache策略组成。
#     Scrapy提供了两种HTTP缓存存储后端:1、Filesystem storage backend (默认值)  2、DBM storage backend
#     'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
# }
#
# 是否启用Redirect中间件。
# REDIRECT_ENABLED = True
# 单个request被重定向的最大次数
# REDIRECT_MAX_TIMES=20


# 可用的插件列表。需要注意，有些插件需要通过设定来启用。
# 默认情况下， 该设定包含所有稳定(stable)的内置插件。
# EXTENSIONS_BASE={
#     'scrapy.contrib.corestats.CoreStats': 0,
#     'scrapy.telnet.TelnetConsole': 0,
#     'scrapy.contrib.memusage.MemoryUsage': 0,
#     'scrapy.contrib.memdebug.MemoryDebugger': 0,
#     'scrapy.contrib.closespider.CloseSpider': 0,
#     'scrapy.contrib.feedexport.FeedExporter': 0,
#     'scrapy.contrib.logstats.LogStats': 0,
#     'scrapy.contrib.spiderstate.SpiderState': 0,
#     'scrapy.contrib.throttle.AutoThrottle': 0,
# }
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# 保存项目中启用的1、插件及2、其顺序的3、字典。
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 保存项目中启用的1、pipeline及2、其顺序的3、字典。
# 该字典默认为空，值(value)任意。 不过值(value)习惯设定在0-1000范围内。
#ITEM_PIPELINES = {
#    'weibouser.pipelines.WeibouserPipeline': 300,
#}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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


# Enable and configure HTTP caching (disabled by default) HTTPCache中间件设置
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True # HTTP缓存是否开启。
#HTTPCACHE_EXPIRATION_SECS = 0 # 缓存的request的超时时间，单位秒。 超过这个时间的缓存request将会被重新下载。如果为0，则缓存的request将永远不会超时。
#HTTPCACHE_DIR = 'httpcache'  # 存储(底层的)HTTP缓存的目录。
#HTTPCACHE_IGNORE_HTTP_CODES = [] # 不缓存设置中的HTTP返回值(code)的request。
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage' # 实现缓存存储后端的类。
# Dummpy策略对于测试spider十分有用。其能使spider运行更快(不需要每次等待下载完成)，
# 同时在没有网络连接时也能测试。其目的是为了能够回放spider的运行过程， 使之与之前的运行过程一模一样 。
# 使用这个策略请设置: HTTPCACHE_POLICY 为 scrapy.contrib.httpcache.DummyPolicy


#DOWNLOAD_HANDLERS_BASE={
#     'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
#     'http': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
#     'https': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
#     's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
# }
# 保存项目中默认启用的下载处理器(request downloader handler)的字典
# DOWNLOAD_HANDLERS={}
# 如果需要关闭上面的下载处理器，您必须在项目中的 DOWNLOAD_HANDLERS 设定中设置该处理器，并为其赋值为 None 。 例如，关闭文件下载处理器:
#DOWNLOAD_HANDLERS = {
#     'file': None,
# }

# 用于检测过滤重复请求的类。默认: 'scrapy.dupefilter.RFPDupeFilter'
# 默认的 (RFPDupeFilter) 过滤器基于 scrapy.utils.request.request_fingerprint 函数生成的请求fingerprint(指纹)。
# 如果您需要修改检测的方式，您可以继承 RFPDupeFilter 并覆盖其 request_fingerprint 方法。
# 该方法接收 Request 对象并返回其fingerprint(一个字符串)。
# DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'


#是否启用logging。
# LOG_ENABLED = True
# LOG_FILE为设置logging输出的文件名。如果为None，则使用标准错误输出(standard error)。
# LOG_FILE = None
# LOG_STDOUT如果为 True ，进程所有的标准输出(及错误)将会被重定向到log中。
# 例如， 执行 print 'hello' ，其将会在Scrapy log中显示。
# LOG_STDOUT =False