"""
Deep-ML Problem #XX
Title: Derivative of a Polynomial
Category: Calculus
Difficulty: Easy
"""

def poly_term_derivative(c: float, x: float, n: float) -> float:
    return c * n * x ** (n - 1)
