"""
__author__ = '伴月雎'
__time__ = '2021/5/5 13:59'

"""
from time import sleep
from base import Base
browser = "headless"


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
        sleep(2)
