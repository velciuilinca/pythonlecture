# Your testing code
from src.my_math import *

def test_addition():
    result = add_numbers(5,7)
    assert result == 12
def test_substraction():
    result = subtract_numbers(12,10)
    assert result == -2
def test_multiplication():
    result = multiply_numbers(5,7)
    assert result == 35
