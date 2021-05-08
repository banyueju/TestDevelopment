"""
__author__ = '伴月雎'
__time__ = '2021/4/17 10:33'
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

    # 显式等待示例
    def test_explicit_wait1(self):
        # 定义一个方法
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@id="articleMeList-blog"]//a')) >= 1
        # 定义一个显式等待，在10秒内轮询等待wait方法为真执行下一步，否则抛出异常
        # 注意这里wait后不要加括号，表示把self.driver传进来给了它，否则表示为调用了该函数
        WebDriverWait(self.driver, 10).until(wait)

    def test_explicit_wait2(self):
        # 使用selenium自带expected_conditions的很多条件
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(By.XPATH, '//*[@id="articleMeList-blog"]//a'))
