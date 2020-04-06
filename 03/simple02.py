# -*- coding: utf-8 -*-

import re

import sys

reload(sys)

sys.setdefaultencoding('utf-8')

m_match = re.match('com','www.santostang.com');

m_search = re.search('com','www.santostang.com');

print(m_match);

print(m_search);
