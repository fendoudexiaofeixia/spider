#!/usr/bin/python
# -*- coding: UTF-8 -*-
import selenium
from selenium import webdriver
from time import sleep

url = "https://search.jd.com/Search?keyword=freebuds3&suggest=1.his.0.0&wq=freebuds3&page=1&s=53&click=0"

# js = "var q=document.getElementById('id').scrollTop=100000"
browser = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
browser.get(url)
sleep(3)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(1)
url = browser.current_url
print(url)
html = browser.page_source
print(html)
