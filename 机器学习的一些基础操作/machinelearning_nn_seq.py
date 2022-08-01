import torch
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential
from torch.utils.tensorboard import SummaryWriter


class Cx(nn.Module):
    def __init__(self):
        super(Cx, self).__init__()
        self.model1 = Sequential(
            Conv2d(3, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10)
        )
        '''    self.conv1 = Conv2d(3,32,5,padding=2)
        self.maxpool1 = MaxPool2d(2)
        self.conv2 = Conv2d(32,32,5,padding=2)
        self.maxpool2 = MaxPool2d(2)
        self.conv3 = Conv2d(32,64,5,padding=2)
    #IN 32 OUT 64
        self.maxpool3 = MaxPool2d(2)
        self.flatten = Flatten()
        #线形层
        self.linbear1 = Linear(1024,64)
        self.linbear2 = Linear(64,10)'''




    def forward(self, x):
        x = self.model1(x)
        return x

''' x = self.conv1(x)
        经过conv1 再给x
        x=self.maxpool1(x)
        x=self.conv2(x)
        x=self.maxpool2(x)
        x=self.conv3(x)
        x=self.maxpool3(x)
        x=self.flatten(x)
        #可以看看flaten之后的
        #64张图展成1024
        x=self.linbear1(x)
        x=self.linbear2(x)
        return x'''








cx = Cx()
"print(cx)"
#检验网络

input = torch.ones((64,3,32,32))
output = cx(input)
print(output.shape)

#对网络结构进行实验

writer = SummaryWriter('logs_seq')
writer.add_graph(cx, input)
writer.close()