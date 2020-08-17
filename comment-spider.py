#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import requests
# import urllib3
import time
# from selenium import webdriver
import requests
import json
import random


# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_comment_json(page=0):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=66430683946&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % page
    kv = {'referer': 'https://item.jd.com/100013289660.html',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    r = requests.get(url, headers=kv)
    txt = r.text[20:-2]
    r_json = json.loads(txt)
    r_comment = r_json['comments']
    for conten in r_comment:
        with open(r'C:\Users\lixiaodong\Desktop\content.txt', 'a', encoding='utf-8')as wstream:
            wstream.write(conten['content'])
            print(conten['content'])


if __name__ == '__main__':
    for i in range(100):
        get_comment_json(i)
        time.sleep(random.random() * 5)
