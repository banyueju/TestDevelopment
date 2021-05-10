"""
__author__ = '伴月雎'
__time__ = '2021/5/7 23:28'
"""
from test_web_wechat.page.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        main_page = MainPage()
        # 1.跳转到添加成员页面        2.添加成员      3.成员列表
        main_page.goto_add_member().add_member().get_contact_list()

    def test_goto_contact(self):
        main_page = MainPage()
        main_page.goto_contact().get_contact_list()
