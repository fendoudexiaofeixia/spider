#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import requests
# import urllib3
import time
# from selenium import webdriver
import requests
import json
import random
from jingdong import JD
import threading


# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_comment_json(pid, page=0):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=%s&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % (
        pid, page)
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


def get_pid1():
    for pid in JD.return_id():
        for i in range(1, 20, 2):
            try:
                get_comment_json(pid[2:], i)
                time.sleep(random.random() * 5)
                print('-------------------这是线程   1-------------------')
            except:
                print('爬取失败')
    # return 0


def get_pid2():
    for pid in JD.return_id():
        for i in range(2, 20, 2):
            try:
                get_comment_json(pid[2:], i)
                time.sleep(random.random() * 5)
                print('--------------------这是线程  2--------------------')
            except:
                print('爬取失败')
    # return 0


if __name__ == '__main__':
    t1 = threading.Thread(target=get_pid1, args=())
    t2 = threading.Thread(target=get_pid2, args=())
    # t3 = threading.Thread(target=main, args=())
    t1.start()
    t2.start()
    # t3.start()
    t1.join()
    t2.join()
    # t3.join()
