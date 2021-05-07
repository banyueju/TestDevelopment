"""
__author__ = '伴月雎'
__time__ = '2021/5/7 18:24'
"""
from base import Base
from time import sleep


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("D:\\ChromeDownload\\picture\\pythonlogo.jpg")
        sleep(3)

