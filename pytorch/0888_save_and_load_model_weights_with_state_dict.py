"""
Deep-ML Problem #888
Title: Save and Load Model Weights with state_dict
Category: pytorch
Difficulty: Easy
"""

import io
import torch
import torch.nn as nn

def copy_weights(src: nn.Module, dst: nn.Module) -> nn.Module:
    # TODO: serialize src's state dict into a buffer, rewind, then load it into dst

    buff = io.BytesIO()

    torch.save(src.state_dict(), buff)

    buff.seek(0)

    state_dict = torch.load(buff)

    dst.load_state_dict(state_dict)
