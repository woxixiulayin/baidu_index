#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from selenium import webdriver


my_username = 'ganggegedahuB'
my_password = 'liu7536308'

index_addr = 'http://index.baidu.com/?tpl=trend&word=%CC%EC%C6%F8'


def get_shot_screen(web_addr, shot_name="shot.png"):
    global my_username, my_password
    browser = webdriver.Firefox()
    browser.set_window_size(1600, 900)
    browser.get("http://wappass.baidu.com/")
    browser.implicitly_wait(1)
    browser.find_element_by_id("login_username").send_keys(my_username)
    browser.find_element_by_id("login_loginpass").send_keys(my_password)
    time.sleep(2)
    browser.find_element_by_name("submit").click()
    time.sleep(2)
    browser.get(web_addr)
    time.sleep(3)
    browser.save_screenshot(shot_name)
    browser.quit()

if __name__ == '__main__':
    get_shot_screen(index_addr)