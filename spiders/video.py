#!/usr/bin/env python
# encoding: utf-8
"""
File Description:
Author: nghuyong
Mail: nghuyong@163.com
Created Time: 2020/4/14
"""
import re
from scrapy import Selector, Spider
from scrapy.http import Request
from scrapy.shell import inspect_response
from lxml.html import etree
import time
import json
from items import weibovideoItem


class VideoSpider(Spider):
    name = "video"
    base_url = "https://s.weibo.com/"
    allowed_domain=['s.weibo.com','weibo.com']
    # https://s.weibo.com/weibo?q=%23%E7%BE%8E%E5%A5%B3&sudaref=s.weibo.com&page=2

    def start_requests(self):
        keys = ['美女']
        urls = [f'{self.base_url}weibo?q=%23{key}&sudaref==s.weibo.com&page=' for key in keys]
        headers={
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
  'Cookie': 'SINAGLOBAL=3762728309341.974.1643475551958; UOR=,,www.baidu.com; SSOLoginState=1658043697; _s_tentry=-; Apache=5024335155565.665.1658147584064; ULV=1658147584257:17:1:1:5024335155565.665.1658147584064:1653833382856; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Il4DJWM_fxzm436ObB32s5JpX5KMhUgL.FoqfS024SK.4eon2dJLoI7RLxK-LBo5L129NqPxoI5tt; ALF=1690090091; SCF=AtVpMW-LtWR0vAUqymFpu7kORb1pwSXmc_OUidT2uk9TreM4OyxTO211lqkPlbmZwv6GMtfoKg0laSg-_crDrgg.; SUB=_2A25P3_agDeRhGeBL7FMY9SfFyTSIHXVsrW9orDV8PUNbmtANLXb6kW9NRvUjOnBi83GDhOhj8Enk1MtLnJJQ0HHd',
}
        for url in urls:
            for j in range(12,15):
                yield Request(url+str(j), callback=self.parse,headers=headers)


        # for url in urls:
        #     yield Request(url, callback=self.parse)

    def parse(self, response):
        # inspect_response(response,self)
        self.logger.info('psrse开始解析%s',response.url)
        video_urls = response.xpath("//a[@class='WB_video_h5']/video-player").extract()
        urls = []
        # name = response.xpath("//div[@class='content']/div[@class='info']/div[2]/a/text()").extract()
        for i in video_urls:
            url = 'https:' + re.findall(r"src:'(.*?)'", i)[0]
            url = url.replace('amp;','')
            urls.append(url)
        item = weibovideoItem()
        item['video_urls'] = urls
        self.logger.info('数量:%s',str(len(urls)))
        yield item



