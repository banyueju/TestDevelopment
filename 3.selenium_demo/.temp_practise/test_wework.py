"""
__author__ = '伴月雎'
__time__ = '2021/4/17 22:12'
"""
import yaml
from selenium import webdriver
from time import sleep


# 复用浏览器 Chrome --remote-debugging-port=9222
from selenium.common.exceptions import ElementNotInteractableException


class TestWework:
    def test_wework(self):
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


def test_cookie():
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850285961647'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'swgK3L7LMLhyC8j-UCSEQqZZrtbPvQY8k9ouhRDH4TRRuhLAlh1bXlC72OxZ4NOBabx_iojkOCh4plBfW-_Fj6P9Jk91xilpaWikhKeufD0oja6Ufb0It_4uab8Tp-qNuTiBWiKjUEBd-k3rI5ArZeZxS43UNi8CX6VXdriX2tAHNSwTwWHsbqBBUS3AMt74YAcQiM3OY6Bib8gr9bTnHmWqIh1ASr05ab3UsV-QwFrJZu0yE4J2Z3LueUPT-cy94I-4CPfDkLoGppu92sSh9w'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850285961647'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325030446700'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650207432, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618668212,1618671433'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'sites'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6255919'}, {'domain': '.qq.com', 'expiry': 1618798608, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1465776708.1618668213'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618743725, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8484j5k'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3266476919988433'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Itn-fY21mhuHW0RMZIWE_nSNPZojeRSwOooEKI_uxL3VEy21BysQhvelAFt07lAE'}, {'domain': '.qq.com', 'expiry': 1681784208, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.954978227.1618668213'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650203997, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621304268, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
    sleep(5)


def test_cookie_v2():
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    driver.implicitly_wait(10)
    with open('data.yaml',encoding='UTF-8') as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
    try:
        driver.find_element_by_xpath('//*[@id="js_contacts42"]/div/div[2]/div/div[2]/div[2]/div[2]/a[1]').click()
    except ElementNotInteractableException:
        driver.find_element_by_link_text("添加成员").click()
    # 填写姓名
    driver.find_element_by_xpath('//*[@name="username"]').send_keys("Hogwarts_tester")
    # 填写账号
    driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys('384399756@qq.com')
    # 填写邮箱
    driver.find_element_by_xpath('//*[@id="memberAdd_mail"]').send_keys('384399756@qq.com')
    driver.find_element_by_link_text('保存').click()

