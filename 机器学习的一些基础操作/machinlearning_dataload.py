import torchvision

#准备的测试数据集
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_data = torchvision.datasets.CIFAR10("dataset",train=False,transform=torchvision.transforms.ToTensor())

test_loader = DataLoader(dataset = test_data,batch_size=64,shuffle=True,drop_last=False)
#测试数据第一张图片
#dataloader（batch——size=4 取4个数据进行打包 ——image 0123 target
#shuffle=True 就是把数据打乱
#drop_last=False 如果数据不能整除，就把最后一个数据拿出来
#这里的数据是一个list，里面是tensor，tensor是一个三维的数据，

img,target = test_data[0]
print(img.shape)
print(target)

writer = SummaryWriter("dataloader")
step  =0
for data in test_loader:
    img,targets = data
 #   print(img.shape)
  #  print(targets)
    writer.add_images("test_data",img,step)
    step = step +1
writer.close()
