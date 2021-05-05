"""
__author__ = '伴月雎'
__time__ = '2021/5/5 11:57'
"""
from time import sleep
from base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("18912341234")
        sleep(2)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("logo_username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("logo_password")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(2)

