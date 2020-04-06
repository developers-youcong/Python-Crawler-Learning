# -*- coding: utf-8 -*-

import requests

r = requests.get('http://www.santostang.com/')

print("文本编码:".encode('utf-8'),r.encoding)

print("响应状态编码:",r.status_code);

print("字符串方式的响应:",r.text);
