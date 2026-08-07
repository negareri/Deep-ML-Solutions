"""
Deep-ML Problem #22
Title: Sigmoid Activation Function Understanding
Category: Deep Learning
Difficulty: Easy
"""

import math

def sigmoid(z: float) -> float:
    
    return 1/(1 + math.exp(-z))
