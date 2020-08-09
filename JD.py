#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import json
import time
import urllib3
import lxml

PRODUCT_ID = re.compile(r'<strong class="[A-Z]\_[0-9]*" data-done="1">')
PRICES = re.compile(r'<i>[0-9]*.00</i>')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_page_front_html():
    url = 'https://search.jd.com/Search?keyword=freebuds3&suggest=1.his.0.0&wq=freebuds3&page=1&s=53&click=0'
    kv = {'User-Agent': 'Mozilla/5.0',
          'Referer': 'https://www.jd.com/'}
    resp = requests.get(url, headers=kv, verify=False)
    if resp.status_code == 200:
        bs0bj = BeautifulSoup(resp.content, features='lxml')
        return bs0bj




def get_id(content, pattern):
    product = pattern.search(str(content))
    if product:
        return re.findall(r'J_[0-9]*', product[0])[0]
        # return product[0]


def get_prices(number):
    prices_url = requests.get('https://p.3.cn/prices/mgets?skuIds=' + str(number))
    if prices_url.status_code == 200:
        soup = json.loads(prices_url.content)
        return soup[0]['p']


if __name__ == '__main__':
    a = get_page_front_html()
    al = a.findAll('div', {'class': 'p-price'})
    for i in al:
        product_id = get_id(i, PRODUCT_ID)
        prices = get_prices(product_id)
        print('商品编号为：', product_id, '商品价格为：', prices)