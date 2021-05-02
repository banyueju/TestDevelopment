"""
__author__ = '伴月雎'
__time__ = '2021/4/17 22:12'
"""
import os
import yaml
from selenium import webdriver


# 复用浏览器： Chrome --remote-debugging-port=9222
class TestWework:
    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        # 在当前页面点击通讯录
        self.driver.find_element_by_css_selector('#menu_contacts > span').click()
        cookie = self.driver.get_cookies()
        with open('data.yaml', 'w', encoding='UTF-8') as f:
            yaml.dump(cookie, f)


class TestAddPerson:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
        os.remove('data.yaml')

    def test_wework_add_person(self):
        with open('data.yaml', encoding='UTF-8') as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        self.driver.find_element_by_link_text("添加成员").click()
        # 填写姓名
        self.driver.find_element_by_xpath('//*[@name="username"]').send_keys("Hogwarts_tester")
        # 填写账号
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys('384399756@qq.com')
        # 填写邮箱
        self.driver.find_element_by_xpath('//*[@id="memberAdd_mail"]').send_keys('384399756@qq.com')
        # 填完后保存
        self.driver.find_element_by_link_text('保存').click()
