import torch
from torch import nn
from torch.nn import ReLU, Sigmoid, Sequential, Conv2d, Flatten, Linear
import torch
import torchvision
from torch import nn
from torch.nn import MaxPool2d
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10("../data_set1", train= False, download=True\
                                 , transform= torchvision.transforms.ToTensor())

dataloader = DataLoader(dataset,batch_size=1)

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
    def forward(self, x):
        x = self.model1(x)
        return x

loss = nn.CrossEntropyLoss()
cx =Cx()
optim = torch.optim.SGD(cx.parameters(),lr=0.01)



scheduler = StepLR (optim,step_size=10,gamma=0.1)
#随机梯度下降
for epoch in range(20):
    running_loss = 0.0
    for data in dataloader:
        imgs ,targets = data
        outputs = cx(imgs)
        result_loss= loss(outputs,targets)
        #梯度等于0
        optim.zero_grad()
        result_loss.backward()
        scheduler.step()
        running_loss = running_loss + result_loss
    print(running_loss)

