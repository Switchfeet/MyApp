import pytest


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a, b]
