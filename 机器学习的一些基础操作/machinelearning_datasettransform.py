import torchvision

# 转成tensor 数据类型
from torch.utils.tensorboard import SummaryWriter

dataset_transform=  torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
    ])

#下载数据集
train_set = torchvision.datasets.CIFAR10(root = "./dataset", train=True,transform=dataset_transform,download= True)
test_set = torchvision.datasets.CIFAR10(root = "./dataset", train=False,transform=dataset_transform,download= True)

#print(test_set[0])

#img,target = test_set[14]
#img.show()

#CIFAR10数据集 有动物和机械

#print(test_set[0])

writer =SummaryWriter("p10")
for i in range(10):
    img , target = test_set[i]
    writer.add_image("image",img,i)
#img 类型为tensor
##生成的文件丢到p10文件夹下
writer.close()