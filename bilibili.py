#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json

from selenium.webdriver import ActionChains

browser = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
url = 'https://live.bilibili.com/22357580?visit_id=8dc5pifa4ik0'
while True:
    a = []
    browser.get(url)
    time.sleep(20)
    html = browser.page_source
    # b = browser.find_elements_by_xpath('html/body/div/main/div/section/div/div/div/div/div[@class="chat-item danmaku-item "]')
    soup = BeautifulSoup(html, 'lxml')
    cls = soup.find_all('span', attrs={'class': 'danmaku-content v-middle pointer ts-dot-2 open-menu'})
    # print(cls)
    for _ in cls:
        if _.string == (lambda i: a for i in a):
            continue
        else:
            a.append(_.string)
            # print(_.string)
    print(a)
