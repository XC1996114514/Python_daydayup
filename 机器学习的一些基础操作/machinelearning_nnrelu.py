import torch
from torch import nn
from torch.nn import ReLU, Sigmoid
import torch
import torchvision
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10("../data", train= False, download= True
                                 , transform= torchvision.transforms.ToTensor())

dataloader = DataLoader(dataset,batch_size=64)

class Cx(nn.Module):
    def __init__(self):
        super(Cx,self).__init__()
        self.relu1 = ReLU()
        self.sigmopid1 = Sigmoid()
    def forward(self,input):
        output = self.relu1(input)
        return output

cx=Cx()

writer =SummaryWriter("../logs_relu")
step = 0
for data in dataloader:
    imgs ,targets = data
    writer.add_images("input",imgs,global_step=step)
    output = cx(imgs)
    writer.add_images("output",output,step)
    step+=1
writer.close()