"""
__author__ = '伴月雎'
__time__ = '2021/4/9 07:59 下午'
"""
import allure
import pytest
from decimal import Decimal, InvalidOperation, DivisionByZero


@allure.feature('计算器加法除法测试')
class TestCalculate:
    @pytest.mark.last
    def test_add(self, initcalc_class, get_add_data):
        print(get_add_data[0])
        try:
            assert Decimal(str(get_add_data[3])) == initcalc_class.add(Decimal(str(get_add_data[1])), Decimal(str(get_add_data[2])))
        except InvalidOperation:
            pytest.xfail(reason='不能包含非数值类型！')

    @pytest.mark.run(order=1)
    def test_div(self, initcalc_class,  get_div_data):
        print(get_div_data[0])
        try:
            assert Decimal(str(get_div_data[3])) == initcalc_class.div(Decimal(str(get_div_data[1])), Decimal(str(get_div_data[2])))
        except DivisionByZero:
            pytest.xfail(reason='除数不能为零！')
        except InvalidOperation:
            pytest.xfail(reason='不能包含非数值类型！')
