from ops import *


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(10, 5) == 2


def test_modulus():
    assert modulus(-10) == 10


def test_percentage():
    assert percentage(1000,10) == 100
