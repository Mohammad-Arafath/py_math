# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:08:35 2025

@author: mzamankhan1
"""

import pytest
from MathUtils import MathUtils  # Assuming MathUtils is saved in math_utils.py

@pytest.fixture
def math_utils():
    """Fixture to provide an instance of MathUtils."""
    return MathUtils()

def test_add(math_utils):
    assert math_utils.add(3, 3) == 7
    assert math_utils.add(-3, -2) == -5
    assert math_utils.add(0, 5) == 5
    assert math_utils.add(5, -2) == 3

def test_subtract(math_utils):
    assert math_utils.subtract(10, 4) == 6
    assert math_utils.subtract(-5, -2) == -3
    assert math_utils.subtract(0, 7) == -7
    assert math_utils.subtract(3, 5) == -2

def test_multiply(math_utils):
    assert math_utils.multiply(4, 3) == 12
    assert math_utils.multiply(-4, 3) == -12
    assert math_utils.multiply(0, 10) == 0
    assert math_utils.multiply(5, -2) == -10

def test_divide(math_utils):
    assert math_utils.divide(10, 2) == 5.0
    assert math_utils.divide(-10, 2) == -5.0
    assert math_utils.divide(0, 5) == 0.0
    assert math_utils.divide(10, 0) == -1.0  # Division by zero should return -1.0

if __name__ == "__main__":
    pytest.main()
