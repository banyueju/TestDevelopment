"""
__author__ = '伴月雎'
__time__ = '2021/4/17 10:33'
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(3)
        self.driver.get('http://home.testing-studio.com/')

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        sleep(5)
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        sleep(3)
