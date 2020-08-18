#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import re
import json
import time
import urllib3
from selenium import webdriver

# PRODUCT_ID = re.findall(r'<strong class="[A-Z]\_[0-9]*" data-done="1">')
# PRICES = re.findall(r'<i>[0-9]*.00</i>')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_url(n=1):
    url = "https://search.jd.com/Search?keyword=freebuds3&suggest=1.his.0.0&wq=freebuds3&page=%s&s=53&click=0" % n

    # js = "var q=document.getElementById('id').scrollTop=100000"
    browser = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
    browser.get(url)
    time.sleep(3)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    html = browser.page_source
    browser.close()
    return html


def get_id(content):
    product = re.findall(r'<strong class="[A-Z]\_[0-9]*" data-done="1">', content)
    if product:
        # return re.findall(r'J_[0-9]*', product[0])[0]
        return product


def get_prices(number):
    prices_url = requests.get('https://p.3.cn/prices/mgets?skuIds=' + str(number))
    if prices_url.status_code == 200:
        soup = json.loads(prices_url.content)
        return soup[0]['p']


def return_id():
    for n in range(1, 117, 2):
        a = get_url(n)
        # al = a.findAll('div', {'class': 'p-price'})
        # print(a)
        for i in get_id(a):
            product_id = re.findall(r'J_[0-9]*', i)[0]
            yield product_id

# if __name__ == '__main__':
#     for n in range(1, 117):
#         a = get_url(n)
#         # al = a.findAll('div', {'class': 'p-price'})
#         # print(a)
#         for i in get_id(a):
#             product_id = re.findall(r'J_[0-9]*', i)[0]
#             prices = get_prices(product_id)
#             print('商品编号为：', re.findall(r'J_[0-9]*', i)[0], '商品价格为：', prices)
#         # print('------------------这是第%s页------------------' % n)
