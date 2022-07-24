# coding:utf-8

import scrapy
from scrapy import Selector, Spider
from scrapy.http import Request
from scrapy.shell import inspect_response
from items import weiboimageItem


class Image_Spider(Spider):
    name = 'images_spider'
    allowed_domain = ['s.weibo.com']
    base_url = 'https://s.weibo.com/weibo?q={#待输入的微博话题#}&nodup=1&page='

    def start_requests(self):
        for i in range(1,51):
            yield Request(self.base_url + str(i), callback=self.parse)

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

