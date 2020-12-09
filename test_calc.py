import pytest
from pythoncode.calculator import Calculator


class TestCal:

    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a, b, expect", [(3, 5, 8), (-1, -2, -3), (100, 200, 300)], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a, b, expect", [(8, 5, 3), (-1, -2, 1), (300, 200, 100)], ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a, b, expect", [(3, 8, 24), (-3, -2, 6), (300, 200, 60000)],
                             ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a, b, expect", [(25, 5, 5), (-6, -2, 3), (300, 50, 6)],
                             ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        assert expect == self.cal.div(a, b)
