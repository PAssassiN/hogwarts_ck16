import pytest


@pytest.fixture(scope="module")
def myfixture(request):
    print("yield之前，开始计算")
    yield
    print("yield之后，计算结束")
