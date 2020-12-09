import pytest


def add_function(a, b):
    return a + b


#
# @pytest.mark.parametrize("a, b, expected", [
#     (3, 5, 8), (-1, -2, -3), (1000, 1000, 2000)])


@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [4, 5, 6])
def test_add(a, b):
    assert add_function(a, b) == a + b
