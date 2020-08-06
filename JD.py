#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import json
import time
import urllib3
from urllib.request import urlopen


def get_page_html(i=1):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = 'https://search.jd.com/Search?keyword=freebuds3&suggest=1.def.0.V12--38s0&wq=freebuds3&page=%s&s=%s&click=0' % (
        i, i + 60)
    kv = {'User-Agent': 'Mozilla/5.0',
          'Referer': 'https://search.jd.com/Search?keyword=freebuds&enc=utf-8&wq=freebuds&pvid=a16fe2a910b14e7695ce194f60c490e5'}
    # for i in range(1, 10, 2):
    resp = requests.get(url, headers=kv, verify=False)
    if resp.status_code == 200:
        bs0bj = BeautifulSoup(resp.content, features='html.parser')
        # time.sleep(1)
        # with open(r'C:\Users\lixiaodong\Desktop\aaa.txt', 'w', encoding='utf8') as wstream:
        #     wstream.write(str(bs0bj))
        return bs0bj
        # prices_id = re.match(_.attrs['id'], '[0-9]*')
        # print(prices_id)


def get_product_id(html):
    product_id = html.findAll('img', {'class': "err-product"})
    for _ in product_id:
        if 'data-sku' and 'class' in _.attrs:
            # print(re.findall(r'[0-9]*', _.attrs['id'])[6])
            # return re.findall(r'[0-9]*', _.attrs['id'])[-2]
            # return _.attrs['data-sku']
            yield _.attrs['data-sku']


def get_prices(product_id):
    js = requests.get('https://p.3.cn/prices/mgets?skuIds=J_' + product_id)
    resp = json.loads(js.content)
    return resp[0]['p']


def page_decode(page_bytes, charsets):
    for charset in charsets:
        try:
            return page_bytes.decode(charset)
        except UnicodeDecodeError:
            pass


def main():
    rep = []
    for i in range(1, 10, 2):
        a = get_page_html(i)
        for n in get_product_id(a):
            rep.append(n)
            print(n)
            # print(get_prices(n))
    # # print(b)

    # print(a)
    # print('********************************************************', i)
    dic = {}.fromkeys(rep)
    # # 这种方法建立字典，会把列表里的元素当做字典的键，由于字典的键不能重复，所以会自动去重
    if len(dic) == len(rep):
        print('列表里的元素互不重复！')
    else:
        print('列表里有重复的元素！')
        print(len(dic), len(rep))



if __name__ == '__main__':
    main()
