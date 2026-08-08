"""
Deep-ML Problem #883
Title: Implement a Linear Layer Forward Pass with Matrix Multiplication
Category: pytorch
Difficulty: Easy
"""

import torch

def linear_forward(x: torch.Tensor, W: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    # TODO: implement y = x W^T + b using PyTorch ops

    if x.shape[1] != W.shape[1]:
        raise ValueError("Incompatible shapes between x and W.")

    if W.shape[0] != b.shape[0]:
        raise ValueError("Bias dimension must match output features.")

    return x @ W.T + b
