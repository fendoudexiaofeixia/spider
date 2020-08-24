#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

desktop = input('请输入你的用户名：')


def OA_start():
    browser = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
    url = 'http://oa.calmcar.com/wui/index.html#/main/portal/portal-2-1?_key=x8ls7p'
    browser.get(url)
    time.sleep(3)
    browser.find_element_by_xpath('.//input[@id="loginid"]').send_keys('13820566030')
    browser.find_element_by_xpath('.//input[@id="userpassword"]').send_keys('1111')
    browser.find_element_by_xpath(".//button[@id='submit']").click()
    time.sleep(3)
    browser.find_element_by_xpath(".//div[@class='singBtn']").click()
    time.sleep(5)
    browser.close()
    return 0


def Date_judgment():
    return time.ctime()


def Logging(deskstop, file):
    with open(r'C:\Users\%s\Desktop\content.txt' % deskstop, 'a', encoding='utf-8')as wstream:
        wstream.write(file + '\n')
        print('记录成功')


if __name__ == '__main__':
    data_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    while True:
        a = Date_judgment()
        print(a)
        if a.split(' ')[0] in data_list and a.split(' ')[3] in ['08:59:00', '19:00:00']:
            OA_start()
            Logging(desktop, a.split(' ')[3])
            # print(a.split(' '))
