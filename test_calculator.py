from Calculator import Calculator
import pytest

@pytest.fixture()
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(3, 4) == 7

def test_sub(calculator):
    assert calculator.subtract(6, 3) == 3

def test_mul(calculator):
    assert calculator.multiply(6, 3) == 18

