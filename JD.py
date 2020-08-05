#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

url = 'https://search.jd.com/s_new.php?keyword=freebuds&wq=freebuds&page=2&s=27&scrolling=y&log_id=1596636759595.7784&tpl=3_M&isList=0&show_items='


def get_page_html(seed_url, charsets=('utf-8',)):
    kv = {'User-Agent': 'Mozilla/5.0',
          'Referer': 'https://search.jd.com/Search?keyword=freebuds&enc=utf-8&wq=freebuds&pvid=a16fe2a910b14e7695ce194f60c490e5'}
    resp = requests.get(seed_url, headers=kv, verify=False)
    if resp.status_code == 200:
        bs0bj = BeautifulSoup(resp.content, features='html.parser')
        id = bs0bj.findAll('div', 'id=')
        # prices = requests.get('https://p.3.cn/prices/mgets?skuIds=J_')
        print(bs0bj, id)


def page_decode(page_bytes, charsets):
    for charset in charsets:
        try:
            return page_bytes.decode(charset)
        except UnicodeDecodeError:
            pass


if __name__ == '__main__':
    get_page_html(url)
