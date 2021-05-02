"""
__author__ = '伴月雎'
__time__ = '2021/4/17 9:45'
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestBaidu:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com/")

    def teardown(self):
        self.driver.quit()

    def test_baidu_first(self):
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "su").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院 - 主页").click()
