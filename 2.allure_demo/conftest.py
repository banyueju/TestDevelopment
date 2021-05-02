"""
__author__ = '伴月雎'
__time__ = '2021/4/12 22:37'
"""
from typing import List
import allure
import pytest
import yaml
from calculator import Calculator


@pytest.fixture(scope='class')
def initcalc_class():
    print("\n【-----测试开始-----】")
    calculus = Calculator()
    yield calculus
    print("\n【-----测试结束-----】")


@pytest.fixture(params=yaml.safe_load(open("./case_data.yaml", 'r', encoding='utf-8'))['add_data'],
                ids=[i[0] for i in yaml.safe_load(open("./case_data.yaml", 'r', encoding='utf-8'))['add_data']])
def get_add_data(request):
    print("\n【计算开始】")
    yield request.param
    print("【计算结束】")


@pytest.fixture(params=yaml.safe_load(open("./case_data.yaml", 'r', encoding='utf-8'))['div_data'],
                ids=[i[0] for i in yaml.safe_load(open("./case_data.yaml", 'r', encoding='utf-8'))['div_data']])
def get_div_data(request):
    print("\n【计算开始】")
    yield request.param
    print("【计算结束】")


def pytest_collection_modifyitems(session, config, items: List):
    print("这是收集所有测试用例的方法")
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'test_div' in item.name:
            item.add_marker(allure.story('除法计算'))
        elif 'test_add' in item.name:
            item.add_marker(allure.story('加法计算'))
    print(items)


def pytest_addoption(parser):
    parser.addoption("--env",
                     default="test",
                     dest="env",
                     help="set test run env")
