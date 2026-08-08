"""
Deep-ML Problem #882
Title: Add a Bias Vector to a Batch via Broadcasting
Category: pytorch
Difficulty: Easy
"""

import torch

def add_bias(x: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    # TODO: add b to every row of x using broadcasting
    
    if x.shape[1] != b.shape[0]:
        raise ValueError("Incompatible shapes.")
    
    return x + b
