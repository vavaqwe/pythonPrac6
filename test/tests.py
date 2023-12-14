from app import calculator
import pytest


@pytest.fixture
def calculator_instance():
    return calculator.Calculator(10, 2)

def test_plus_first(calculator_instance):
    result = calculator_instance.plus()
    assert result == 12

def test_plus_second(calculator_instance):
    result = calculator_instance.plus()
    assert isinstance(result, int)

def test_minus_first(calculator_instance):
    result = calculator_instance.minus()
    assert result == 8

def test_minus_second(calculator_instance):
    result = calculator_instance.minus()
    assert isinstance(result, int)

def test_division_first(calculator_instance):
    result = calculator_instance.division()
    assert result == 5

def test_division_second(calculator_instance):
    result = calculator_instance.division()
    assert isinstance(result, float)

def test_multiplication_first(calculator_instance):
    result = calculator_instance.multiplication()
    assert result == 20

def test_multiplication_second(calculator_instance):
    result = calculator_instance.multiplication()
    assert isinstance(result, int)

def test_degree_first(calculator_instance):
    result = calculator_instance.degree()
    assert result == 100

def test_degree_second(calculator_instance):
    result = calculator_instance.degree()
    assert isinstance(result, float)

def test_arithmetic_first(calculator_instance):
    result = calculator_instance.arithmetic()
    assert isinstance(result, int)

