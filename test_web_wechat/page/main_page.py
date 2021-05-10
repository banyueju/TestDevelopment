"""
__author__ = '伴月雎'
__time__ = '2021/5/7 23:08'
"""
from test_web_wechat.page.add_member import AddMemberPage
from test_web_wechat.page.contact import ContactPage
import yaml
from selenium import webdriver


class MainPage:
    """
    用公共方法代表UI所提供的功能
    """

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        return ContactPage()

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        return AddMemberPage()
