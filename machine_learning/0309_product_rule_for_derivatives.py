"""
Deep-ML Problem #309
Title: Product Rule for Derivatives
Category: Machine Learning
Difficulty: Medium
"""

import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    def deriv(c):
        result = []
        for i in range(1, len(c)):
            result.append(c[i] * i)

        if len(result) == 0:
            return [0]

        return result

    def multiply(a, b):
        result = [0] * (len(a) + len(b) - 1)

        for i in range(len(a)):
            for j in range(len(b)):
                result[i + j] += a[i] * b[j]

        return result

    def add(a, b):
        result = [0] * max(len(a), len(b))

        for i in range(len(result)):
            if i < len(a):
                result[i] += a[i]

            if i < len(b):
                result[i] += b[i]

        return result

    result = add(
        multiply(deriv(f_coeffs), g_coeffs),
        multiply(deriv(g_coeffs), f_coeffs)
    )

    result = [round(float(x), 4) for x in result]

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    if result == [0]:
        return [0.0]

    return result
