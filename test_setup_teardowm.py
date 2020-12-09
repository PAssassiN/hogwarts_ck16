import pytest


class TestClass():

    def setup_class(self):
        print("setup类里面的所有用例开始执行\n")

    def teardown_class(self):
        print("teardown类里面的所有用例结束执行\n")

    def setup_method(self):
        print("setup的每个用例开始执行\n")

    def teardown_method(self):
        print("teardown的每个用例结束执行\n")

    def test_one(self):
        print("test_one")

    def test_two(self):
        print("test_two")
