"""
__author__ = '伴月雎'
__time__ = '2021/5/4 16:24'
"""
from selenium import webdriver
from selenium.webdriver import TouchActions
from time import sleep


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        """
        打开Chrome
        打开URL:http://www.baidu.com
        向搜索框输入'selenium测试'
        通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        """
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el, 0, 8000).perform()
        # sleep(3)
