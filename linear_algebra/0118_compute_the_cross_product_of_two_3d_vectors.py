"""
Deep-ML Problem #118
Title: Compute the Cross Product of Two 3D Vectors
Category: Linear Algebra
Difficulty: Easy
"""

def cross_product(a, b):
    i = a[1] * b[2] - a[2] * b[1]
    j = a[2] * b[0] - a[0] * b[2]
    k = a[0] * b[1] - a[1] * b[0]
    return [i, j, k]
