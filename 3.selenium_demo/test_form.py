"""
__author__ = '伴月雎'
__time__ = '2021/5/4 17:04'
"""
from selenium import webdriver
from time import sleep


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        button = self.driver.find_element_by_id("user_remember_me")
        self.driver.execute_script("$(arguments[0]).click()", button)
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(5)
