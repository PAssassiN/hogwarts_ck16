import pytest


class Test_demo():
    def test_one(self):
        print("执行test_one")
        assert 1 + 1 == 2

    def test_two(self, myfixture):
        print("执行test_two")
        # 分别打印myfixture 传回来的参数
        print(myfixture)
        assert 1 + 1 == 2

    def test_three(self):
        print("执行test_three")
        assert 1 + 1 == 2
