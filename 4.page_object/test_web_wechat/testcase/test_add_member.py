"""
__author__ = '伴月雎'
__time__ = '2021/5/7 23:28'
"""
from test_web_wechat.page.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        MainPage().goto_add_member().add_member().get_contact_list()
