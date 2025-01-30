# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:31:47 2025

@author: mzamankhan1
"""

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return -1.0  # Handle division by zero
        return a / b

# Example usage:
if __name__ == "__main__":
    math_utils = MathUtils()
    print(f"Addition: {math_utils.add(5, 3)}")
    print(f"Subtraction: {math_utils.subtract(5, 3)}")
    print(f"Multiplication: {math_utils.multiply(5, 3)}")
    print(f"Division: {math_utils.divide(5, 0)}")  # Should return -1.0
    print(f"Division: {math_utils.divide(10, 2)}")  # Should return 5.0
