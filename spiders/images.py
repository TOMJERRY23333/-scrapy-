# coding:utf-8
"""
获取微博图片练习
author: 李灏城
"""

import scrapy
from scrapy import Selector, Spider
from scrapy.http import Request
from scrapy.shell import inspect_response
from items import weiboimageItem


class Image_Spider(Spider):
    name = 'images_spider'
    allowed_domain = ['s.weibo.com']
    base_url = 'https://s.weibo.com/weibo?q=%23%E6%AF%8F%E6%97%A5%E4%B8%80%E8%85%BF%23&nodup=1&page='
    # start_urls = ['https://s.weibo.com/weibo?q=%23%E6%AF%8F%E6%97%A5%E4%B8%80%E8%85%BF%23&nodup=1&page=1']
    # heads = header = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
    #     'cookie': 'SINAGLOBAL=3762728309341.974.1643475551958; UOR=,,www.baidu.com; SSOLoginState=1658043697; _s_tentry=-; Apache=5024335155565.665.1658147584064; ULV=1658147584257:17:1:1:5024335155565.665.1658147584064:1653833382856; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Il4DJWM_fxzm436ObB32s5JpX5KMhUgL.FoqfS024SK.4eon2dJLoI7RLxK-LBo5L129NqPxoI5tt; ALF=1689845731; SCF=AtVpMW-LtWR0vAUqymFpu7kORb1pwSXmc_OUidT2uk9To13TgPc-BDBixwRe1NzN3VWEBWQdLehuzKW0uWE1Z8U.; SUB=_2A25P07w5DeRhGeBL7FMY9SfFyTSIHXVsqKrxrDV8PUNbmtANLUylkW9NRvUjOigcikDf1aD9esFJTsHBUN3j3CJY'}

    def start_requests(self):
        urls = 'https://s.weibo.com/weibo?q=%23%E6%AF%8F%E6%97%A5%E4%B8%80%E8%85%BF%23&nodup=1&page='
        for i in range(1,51):
            yield Request(urls + str(i), callback=self.parse)

    def parse(self, response):
        # inspect_response(response, self)
        self.log('A response from %s just arrived!' % response.url)
        selector = Selector(response)
        url_list = selector.xpath("//div[@class='media media-piclist']/ul/li/img/@src").extract()
        urls = []
        for i in url_list:
            i = i.replace('/orj360/', '/mw1024/')
            i = i.replace('/thumb150/', '/mw1024/')
            i = i.replace('/thumb180/', '/mw1024/')
            urls.append(i)
        item = weiboimageItem()
        item['image_urls'] = urls
        yield item
        # request_meta = response.meta
        # request_meta['item'] = item
        # for i in range(2, 51):
        #     yield Request(self.base_url + str(i), callback=self.parse_further, meta=request_meta)

    # def parse_further(self, response):
    #     item = response.meta['item']
    #     # inspect_response(response, self)
    #     self.log('A response from %s just arrived!' % response.url)
    #     selector = Selector(response)
    #     url_list = selector.xpath("//div[@class='media media-piclist']/ul/li/img/@src").extract()
    #     urls = []
    #     for i in url_list:
    #         url = i.replace('/orj360/', '/mw1024/').replace('/thumb180/', '/mw1024/')
    #         urls.append(url)
    #     item['image_urls'] = urls
    #     yield item
