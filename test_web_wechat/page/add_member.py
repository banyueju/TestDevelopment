"""
__author__ = '伴月雎'
__time__ = '2021/5/7 23:09'
"""
from test_web_wechat.page.contact import ContactPage


class AddMemberPage:

    def add_member(self):
        """
        页面的return分成两个部分
        1. 其他页面的实例
        2. 用例所需要的断言

        """
        return ContactPage()

    def add_xxx(self):
        # 调用本身的实例
        return self
