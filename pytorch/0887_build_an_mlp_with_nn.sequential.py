"""
Deep-ML Problem #887
Title: Build an MLP with nn.Sequential
Category: pytorch
Difficulty: Easy
"""

import torch
import torch.nn as nn

def build_mlp(in_dim: int, hidden_dim: int, out_dim: int) -> nn.Sequential:
    # TODO: return a Sequential of Linear -> ReLU -> Linear

    return nn.Sequential(
        nn.Linear(in_dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, out_dim),
        )
    
