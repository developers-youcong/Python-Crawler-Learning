# -*- coding: utf-8 -*-

import requests

import sys

from lxml import etree


reload(sys)

sys.setdefaultencoding('utf-8')

link = "http://www.santostang.com/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'}

r = requests.get(link,headers=headers)


html = etree.HTML(r.text)

title_list = html.xpath('//h1[@class="post-title"]/a/text()')

print(title_list)




