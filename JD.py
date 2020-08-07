#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import json
import time
import urllib3
import lxml


def get_page_front_html(i):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = 'https://search.jd.com/s_new.php?keyword=freebuds3&suggest=1.his.0.0&wq=freebuds3&scrolling=y&log_id=1596809916583.3068&tpl=3_M&isList=0&show_items=&page=' + str(
        2 * i - 1)
    kv = {'User-Agent': 'Mozilla/5.0',
          'Referer': 'https://search.jd.com/Search?keyword=freebuds&enc=utf-8&wq=freebuds&pvid=a16fe2a910b14e7695ce194f60c490e5'}
    resp = requests.get(url, headers=kv, verify=False)
    if resp.status_code == 200:
        bs0bj = BeautifulSoup(resp.content, features='lxml')
        return bs0bj


def get_page_last_html(i):
    a = time.time()
    b = '%.5f' % a
    url = 'https://search.jd.com/s_new.php?keyword=freebuds3&suggest=1.his.0.0&wq=freebuds3&scrolling=y&tpl=3_M&isList=0&show_items=&page=' + str(
        2 * i) + '&s=' + str(48 * i - 20) + '&log_id=' + str(b)
    kv = {'User-Agent': 'Mozilla/5.0',
          'Referer': 'https://search.jd.com/Search?keyword=freebuds&enc=utf-8&wq=freebuds&pvid=a16fe2a910b14e7695ce194f60c490e5'}
    resp = requests.get(url, headers=kv, verify=False)
    if resp.status_code == 200:
        bs0bj = BeautifulSoup(resp.content, features='lxml')
        return bs0bj


def get_id(html):
    product = html.findAll('li', {'class': 'gl-item'})
    for data in product:
        try:
            yield re.findall(r'[0-9]*\.00', str(data.findAll('div', {'class': 'p-price'})))[0]
        except:
            print('失败')


if __name__ == '__main__':
    for _ in range(1, 111):
        res = get_page_front_html(_)
        res1 = get_page_last_html(_)
        for i in get_id(res):
            print(i)
        for n in get_id(res1):
            print(n)
        print('--------------------第%s页-------------------------------------------' % _)
