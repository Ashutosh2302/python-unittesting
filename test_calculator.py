from Calculator import Calculator
import pytest

@pytest.fixture()
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(3, 4) == 7

def test_sub(calculator):
    assert calculator.subtract(6, 3) == 3
