"""
__author__ = '伴月雎'
__time__ = '2021/4/17 9:45'
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestCSDN:
    def setup(self):
        # 实例化一个driver对象
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)
        # 打开一个博客页面
        self.driver.get("https://blog.csdn.net/banyueju")

    def teardown(self):
        # 结束后应当自动关闭浏览器
        self.driver.quit()

    def test_baidu_first(self):
        # xpath方式进行元素定位 并点击
        self.driver.find_element(By.XPATH, '//*[@id="articleMeList-blog"]/div[2]/div[1]/h4/a').click()
        # 强制等待5秒便于人眼观察
        sleep(5)

