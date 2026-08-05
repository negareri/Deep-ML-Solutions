"""
Deep-ML Problem #14
Title: Linear Regression Using Normal Equation
Category: Machine Learning
Difficulty: Easy
"""

import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:

    X = np.array(X)
    y = np.array(y)

    X_T = X.T
    tetha = np.linalg.inv(X_T @ X) @ (X_T @ y)

    return np.round(tetha, 4).tolist()
