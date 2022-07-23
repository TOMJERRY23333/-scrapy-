# from fake_useragent import UserAgent
# import os
# import requests
# from lxml import etree
# import csv
# import re
#
# STORE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) \
#              + '/douban.csv'
# spider_list = []
# url='https://weibo.cn/1087770692/info'
# start_url = ['https://weibo.cn/1087770692/info']
# # for i in range(2, 7):
# #     start_url.append('https://www.jobui.com/rank/company/view/quanguo/?n=' + str(i))
# #     print(start_url)
#
#
#
# def download(url):
#     try:
#         headers = {'User-Agent': str(UserAgent.random())}
#     except AttributeError:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                           'AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/84.0.4147.105 Safari/537.36 ',
#             'Cookie': '_T_WM=fc050dbc4656b2484beb6a9fe854ea52; '
#                       'SCF=AtVpMW-LtWR0vAUqymFpu7kORb1pwSXmc_OUidT2uk9TW5He70cJUQg8-pTzB_s85rUUpy4RW9_QHsH52V4kd_s.; '
#                       'SUB=_2A25P181iDeRhGeBL7FMY9SfFyTSIHXVtO9MqrDV6PUJbktB-LXjlkW1NRvUjOhUl4ncbvkhsSt_Tvt2FPKMwcx3O; '
#                       'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Il4DJWM_fxzm436ObB32s5NHD95QcSKMp1K-41KzRWs4Dqcj1i--fi'
#                       '-z7iKysUc8Xqcnt; SSOLoginState=1658043698'
#         }
#
#     responce = requests.get(url, headers=headers)
#     # responce.encoding = 'utf-8'
#     return responce.text
#
#
# def parse_store(responce):
#     # tree = etree.HTML(responce)
#     #
#     # index_1 = "//div[@class='pl2']/a"
#     # index_2 = "//p[@class='pl']"
#     # index_3 = "//span[@class='rating_nums']"
#
#     tree = etree.HTML(responce.encode('utf-8'))
#
#     com_list_index = 'html/body/div[@class="c"]//text()'
#
#     user_info_text = ";".join(tree.xpath(com_list_index))
#     nick_name = re.findall('昵称;?:?(.*?);', user_info_text)
#     gender = re.findall('性别;?:?(.*?);', user_info_text)
#     place = re.findall('地区;?:?(.*?);', user_info_text)
#     brief_introduction = re.findall('简介;?:?(.*?);', user_info_text)
#     birthday = re.findall('生日;?:?(.*?);', user_info_text)
#     sex_orientation = re.findall('性取向;?:?(.*?);', user_info_text)
#     sentiment = re.findall('感情状况;?:?(.*?);', user_info_text)
#     vip_level = re.findall('会员等级;?:?(.*?);', user_info_text)
#     authentication = re.findall('认证;?:?(.*?);', user_info_text)
#     labels = re.findall('标签;?:?(.*?)更多>>', user_info_text)
#     print(nick_name)
#
#     # for com_url in com_list:
#     #     # url = 'https://www.jobui.com' + com_url
#     #     print(com_url.text)
#
#
#     # title_list = tree.xpath(index_1)
#     # publish_list = tree.xpath(index_2)
#     # score_list = tree.xpath(index_3)
#
#     #/ html[@ class ='ua-windows ua-webkit book-new-nav'] / body / div[@ id='wrapper'] / div[@ id='content'] / div[@ class ='grid-16-8 clearfix'] / div[@ class ='article'] / div[@ class ='indent'] / table[1] / tbody / tr[@ class ='item'] / td[2] / div[@ class ='pl2']
#     #/ html[@ class ='ua-windows ua-webkit book-new-nav'] / body / div[@ id='wrapper'] / div[@ id='content'] / div[@ class ='grid-16-8 clearfix'] / div[@ class ='article'] / div[@ class ='indent'] / table[1] / tbody / tr[@ class ='item'] / td[2] / div[@ class ='pl2']
#     #/ html[@ class ='ua-windows ua-webkit book-new-nav'] / body / div[@ id='wrapper'] / div[@ id='content'] / div[@ class ='grid-16-8 clearfix'] / div[@ class ='article'] / div[@ class ='indent'] / table[1] / tbody / tr[@ class ='item'] / td[2] / div[@ class ='star clearfix'] / span[@ class ='rating_nums']
#     # for i in range(int(len(title_list))):
#     #     title = title_list[i].text.strip()
#     #     publish = publish_list[i].text.strip()
#     #     score = score_list[i].text.strip()
#     #     # 数据流写入
#     #     write.writerow([title, publish, score])
#
#
# if __name__ == '__main__':
#     # 创建csv文件对象
#     # csv_file = open(STORE_PATH, 'w', newline='', encoding='utf-16')
#     # write = csv.writer(csv_file)
#     # write.writerow(["书名", "出版商/作者", "评分", ])
#     res = download(url)
#     parse_store(res)
#     # for i in start_url:
#     #     res = download(i)
#     #     parse_store(res)
#     # csv_file.close()
url = "https://f.video.weibocdn.com/o0/mQhKHes2lx07XPa9scAU010412009Ft30E010.mp4?label=mp4_720p&amp;template=720x1280.24.0&amp;ori=0&amp;ps=1BVp4ysnknHVZu&amp;Expires=1658566161&amp;ssig=Mt%2FG9oqmcs&amp;KID=unistore,video"
url = url.replace('amp;','')
print(url)
