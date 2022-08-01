import torch
import torchvision
from torch import nn
from torch.nn import Conv2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from machinelearning_datasettransform import writer

dataset =  torchvision.datasets.CIFAR10(root='/data1', \
                                 train=False, transform=torchvision.transforms.ToTensor(),download=True, \
                                 )
##直接下载到D盘里了
dataloader = DataLoader(dataset,batch_size=64)
#64打包

class CX(nn.Module):
    def __init__(self):
        super(CX,self).__init__()
        self.conv1 = Conv2d(in_channels =3, out_channels = 6,kernel_size = 3, stride = 1, padding = 0)
     #调conv2d 填参数，彩色图片channel为3
#开始卷积
    def forward(self,x):
        x = self.conv1(x)
        return x
cx = CX()

step = 0
writer = SummaryWriter('D:/python 程序/logs')
for data in dataloader:
    imgs,targets = data
    output = cx(imgs)
    print(imgs.shape)
    print(output.shape)
    writer.add_images("input",imgs,step)
    torch.Size
    #torch.Size([64, 3, 32, 32]) ——》3个channel outchannel 3——》三个卷积核
    #64*6 输出2 个图片，因为输入是3个通道
    output=torch.reshape(output,(-1,3,30,30))
    writer.add_images("output",output,step)
    step = step+1
