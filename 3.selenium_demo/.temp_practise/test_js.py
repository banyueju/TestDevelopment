"""
__author__ = '伴月雎'
__time__ = '2021/5/6 21:31'
"""
from base import Base
from time import sleep
import pytest


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(1)
        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        print(self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a=document.getElementById('train_date');"
                                                  "a.removeAttribute('readonly')")
        self.driver.execute_script('document.getElementById("train_date").value="2021-12-25"')
        sleep(3)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
