import pytest


@pytest.mark.parametrize("a, b, c", [(10, 20, 30), (20, 40, 60), (11, 22, 33), (1, -1, 0)])
def test_add(a, b, c):
    res = a + b
    assert res is c
