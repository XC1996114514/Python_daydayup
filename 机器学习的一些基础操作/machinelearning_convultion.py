import torch
import torch.nn.functional as F
input = torch.tensor([[1,3145,123,43,5],
                       [23,2,43,34,2],
                       [23,41,1,132,65],
                       [23,43,51,32,2],

                      [22,1,3,41,4]])

kernel = torch.tensor([[1,2,1],
                      [0,0,1],
                      [2,1,0]])
#把两个矩阵重新reshape成符合conv2d的形状
input = torch.reshape(input,(1,1,5,5))
kernel = torch.reshape(kernel,(1,1,3,3))
#stride 移动2步骤
#padding 进行填充

output=F.conv2d(input , kernel , stride=2)

print(output)

output2 = F.conv2d(input , kernel , stride=2, padding=1)
print(output2)