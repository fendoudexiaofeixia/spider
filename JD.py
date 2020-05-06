#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import json
import time
from urllib.request import urlopen


def get_page_html(i=1):
    # url = 'https://search.jd.com/s_new.php?keyword=freebuds&wq=freebuds&page=2&s=27&scrolling=y&log_id=1596636759595.7784&tpl=3_M&isList=0&show_items='
    kv = {'User-Agent': 'Mozilla/5.0',
          'Referer': 'https://search.jd.com/Search?keyword=freebuds&enc=utf-8&wq=freebuds&pvid=a16fe2a910b14e7695ce194f60c490e5'}
    # for i in range(1, 10, 2):
    resp = requests.get(
        url='https://search.jd.com/s_new.php?keyword=freebuds&wq=freebuds&page=%s&s=61&scrolling=y&log_id=1596636759595.7784&tpl=3_M&isList=0&show_items=' % i
        , headers=kv, verify=False)
    if resp.status_code == 200:
        bs0bj = BeautifulSoup(resp.content, features='html.parser')
        # time.sleep(1)
        return bs0bj
        # prices_id = re.match(_.attrs['id'], '[0-9]*')
        # print(prices_id)


def get_product_id(html):
    product_id = html.findAll('div')
    for _ in product_id:
        if 'id' in _.attrs:
            # print(re.findall(r'[0-9]*', _.attrs['id'])[6])
            return re.findall(r'[0-9]*', _.attrs['id'])[6]


def get_prices(product_id):
    js = requests.get('https://p.3.cn/prices/mgets?skuIds=J_' + product_id)
    resp = json.loads(js.content)
    return resp[0]['m']


def page_decode(page_bytes, charsets):
    for charset in charsets:
        try:
            return page_bytes.decode(charset)
        except UnicodeDecodeError:
            pass


def main():
    for i in range(1, 50, 2):
        a = get_page_html(i)
        b = get_product_id(a)
        get_prices(b)

        # for a in get_product_id(i):
    # get_product_id(obj)
    #     print(get_prices(a))
    # print(prices_id)


if __name__ == '__main__':
    main()
