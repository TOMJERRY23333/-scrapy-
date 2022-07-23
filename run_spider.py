#!/usr/bin/env python
# encoding: utf-8

import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.video import VideoSpider
from spiders.user import UserSpider
from spiders.images import Image_Spider


if __name__ == '__main__':
    mode = sys.argv[1]
    #什么是环境变量呢？环境变量是程序和操作系统之间的通信方式。
    # 有些字符不宜明文写进代码里，比如数据库密码，个人账户密码，
    # 如果写进自己本机的环境变量里，程序用的时候通过 os.environ.get() 取出来就行了。
    # 这样开发人员本机测试的时候用的是自己本机的一套密码，生产环境部署的时候，用的是公司的公共账号和密码，
    # 这样就能增加安全性。os.environ 是一个字典，是环境变量的字典。
    # 通过os.environ.get(“HOME”)，就可以获取环境变量HOME的值，如果有这个键，返回对应的值；如果没有，返回 none
    os.environ['SCRAPY_SETTINGS_MODULE'] = f'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    mode_to_spider = {
        'user': UserSpider,
        'image': Image_Spider,
        'video':VideoSpider

    }
    process.crawl(mode_to_spider[mode])
    # the script will block here until the crawling is finished
    process.start()
