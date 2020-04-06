# -*- coding: utf-8 -*-

import requests

import sys

from bs4 import BeautifulSoup


reload(sys)

sys.setdefaultencoding('utf-8')

link = "http://www.santostang.com/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'}


r = requests.get(link,headers=headers)

soup = BeautifulSoup(r.text,"lxml")

title = soup.find("h1",class_="post-title").a.text.strip();

print(title)
