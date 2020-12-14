import pytest
from pythoncode.calculator import Calculator
import yaml


def get_data():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        add_data = datas["add"]
        sub_data = datas["sub"]
        mul_data = datas["mul"]
        div_data = datas["div"]
        add_ids = datas["myid"]
        return [add_data, sub_data, mul_data, div_data, add_ids]


class TestCal:
    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a, b, expect", get_data()[0], ids=get_data()[4])
    def test_add(self, a, b, expect, myfixture):
        assert expect == self.cal.add(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b, expect", get_data()[1], ids=get_data()[4])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a, b, expect", get_data()[2], ids=get_data()[4])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b, expect", get_data()[3], ids=get_data()[4])
    def test_div(self, a, b, expect):
        assert expect == self.cal.div(a, b)
