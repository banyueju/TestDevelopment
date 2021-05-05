"""
__author__ = '伴月雎'
__time__ = '2021/5/5 12:00'
"""
from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
