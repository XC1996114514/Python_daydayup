import torch
import torch.nn as nn
from torch import nn



class ChenX96(nn.Module):
   def __init__(self):
    super().__init__()

   def forward(self,input):
        out = input+1
        return out

chenX96 = ChenX96()
x = torch.Tensor(1)
output = chenX96(x)
print(output)
