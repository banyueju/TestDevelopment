"""
__author__ = '伴月雎'
__time__ = '2021/4/9 07:59 下午'
"""
import pytest
import yaml
from calculator import Calculator
from decimal import Decimal


class TestCalculate:
    def setup_class(self):
        self.calculus = Calculator()
        print("\n【------测试开始------】")

    def teardown_class(self):
        print("\n【------测试结束------】")

    def setup(self):
        print("\n【计算开始】")

    def teardown(self):
        print("【计算结束】")

    @pytest.mark.parametrize("name, a, b, result", yaml.safe_load(open("./data_case_add.yaml", 'r', encoding='utf-8')),
                             ids=[i[0] for i in yaml.safe_load(open("./data_case_add.yaml", 'r', encoding='utf-8'))])
    def test_add(self, name, a, b, result):
        print(f"\n本用例名称：{name}")
        assert Decimal(str(result)) == self.calculus.add(Decimal(str(a)), Decimal(str(b)))

    @pytest.mark.parametrize("name, a, b, result", yaml.safe_load(open("./data_case_div.yaml", 'r', encoding='utf-8')),
                             ids=[i[0] for i in yaml.safe_load(open("./data_case_div.yaml", 'r', encoding='utf-8'))])
    def test_div(self, name, a, b, result):
        print(f"\n本用例名称：{name}")
        if b == 0:
            pytest.xfail(reason='除数不能为零！')
        else:
            assert Decimal(str(result)) == self.calculus.div(Decimal(str(a)), Decimal(str(b)))
