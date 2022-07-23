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
from items import WeibouserItem


class UserSpider(Spider):
    name = "user_spider"
    base_url = "https://s.weibo.com/"
    allowed_domain=['s.weibo.com','weibo.com']

    def start_requests(self):
        # user_ids = ['1087770692', '1699432410', '1266321801','1749127163']
        # urls = [f'{self.base_url}/{user_id}/info' for user_id in user_ids]
        headers={
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
  'Cookie': 'SINAGLOBAL=3762728309341.974.1643475551958; UOR=,,www.baidu.com; SSOLoginState=1658043697; XSRF-TOKEN=GRAIcZjkGIel44tN97YyKgxR; _s_tentry=-; Apache=5024335155565.665.1658147584064; ULV=1658147584257:17:1:1:5024335155565.665.1658147584064:1653833382856; UPSTREAM-V-WEIBO-COM=35846f552801987f8c1e8f7cec0e2230; WBPSESS=mgkxesxTEg75-VRgnRx8O482d2btMVGuLHqgyewpQOM93BZoClXhIOc9LqVhAxU6fhceDiJ1cP56nOS87CrX-JS750HogSjf2_G2Wz7LdyG-Pbr336t3dAW0iB0XkB3rkyeOU1Y3RZyIlgyMhynUKw==; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Il4DJWM_fxzm436ObB32s5JpX5KMhUgL.FoqfS024SK.4eon2dJLoI7RLxK-LBo5L129NqPxoI5tt; ALF=1689845731; SCF=AtVpMW-LtWR0vAUqymFpu7kORb1pwSXmc_OUidT2uk9To13TgPc-BDBixwRe1NzN3VWEBWQdLehuzKW0uWE1Z8U.; SUB=_2A25P07w5DeRhGeBL7FMY9SfFyTSIHXVsqKrxrDV8PUNbmtANLUylkW9NRvUjOigcikDf1aD9esFJTsHBUN3j3CJY',
}
        url= 'https://weibo.com/ajax/statuses/hot_band'
        yield Request(url, callback=self.parse,headers=headers)
        # for url in urls:
        #     yield Request(url, callback=self.parse)

    def parse(self, response):

        jsonres = json.loads(response.text)
        list = jsonres['data']['band_list']
        print(list[1]['note'])
        # request_meta = response.meta

        header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
                        'cookie':'SINAGLOBAL=3762728309341.974.1643475551958; UOR=,,www.baidu.com; SSOLoginState=1658043697; _s_tentry=-; Apache=5024335155565.665.1658147584064; ULV=1658147584257:17:1:1:5024335155565.665.1658147584064:1653833382856; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Il4DJWM_fxzm436ObB32s5JpX5KMhUgL.FoqfS024SK.4eon2dJLoI7RLxK-LBo5L129NqPxoI5tt; ALF=1689845731; SCF=AtVpMW-LtWR0vAUqymFpu7kORb1pwSXmc_OUidT2uk9To13TgPc-BDBixwRe1NzN3VWEBWQdLehuzKW0uWE1Z8U.; SUB=_2A25P07w5DeRhGeBL7FMY9SfFyTSIHXVsqKrxrDV8PUNbmtANLUylkW9NRvUjOigcikDf1aD9esFJTsHBUN3j3CJY'}
        # yield Request(self.base_url + 'weibo?q=%23{NAME}%23&page={PAGE}'.format(NAME=list[1]['note'], PAGE=str(1)),
        #               callback=self.parse_further_information, headers=header)
        for item in list:
            name = item['note']
            for i in range(1):
                yield Request(self.base_url + 'weibo?q=%23{NAME}%23&page={PAGE}'.format(NAME=name,PAGE=str(i)),
                          callback=self.parse_further_information, headers=header)


    def parse_further_information(self, response):
        # inspect_response(response, self)
        self.log('A response from %s just arrived!' % response.url)
        selector= Selector(response)

        # tree = etree.HTML(response.text)
        index = "//div[@class='card-feed']/div[@class='content']"
        index_1 = "./p[@class='txt']/text()"
        index_2 = "./div[@class='info']/div[2]/a/text()"

        com_list = selector.xpath(index)

        for item in com_list:
            it = WeibouserItem()
            it['name'] = item.xpath(index_2).extract()[0]
            it['comment'] = ''.join([i.strip() for i in item.xpath(index_1).extract()]).replace('\u200b', '')
            yield it
        #
        #
        # text = response.text
        # user_item = response.meta['item']
        # tweets_num = re.findall('微博\[(\d+)\]', text)
        # if tweets_num:
        #     user_item['tweets_num'] = int(tweets_num[0])
        # follows_num = re.findall('关注\[(\d+)\]', text)
        # if follows_num:
        #     user_item['follows_num'] = int(follows_num[0])
        # fans_num = re.findall('粉丝\[(\d+)\]', text)
        # if fans_num:
        #     user_item['fans_num'] = int(fans_num[0])
        # yield user_item
