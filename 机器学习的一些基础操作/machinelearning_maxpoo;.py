import torch
import torchvision
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10("../data", train= False, download= True
                                 , transform= torchvision.transforms.ToTensor())

dataloader = DataLoader(dataset,batch_size=64)
#只有1个channel



class Cx(nn.Module):
    def __init__(self):
        super(Cx,self).__init__()
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode = True)

    def forward(self,input):
        output = self.maxpool1(input)
        return output
cx=Cx()

writer =SummaryWriter('logs_maxpoole')
step = 0
for data in dataloader:
    imgs, targets =data
    writer.add_images("input",imgs,step)
    output = cx(imgs)
    writer.add_images("output",output,step)
    step+=1

writer.close()