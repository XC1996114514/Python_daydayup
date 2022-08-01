from torch.utils.data import Dataset
import cv2
from PIL import Image
import os
#获取文件夹中的所有图片路径
#文件夹下所有东西变成一个列表
#index 获取文件，先创建文件的列表
#os.path.join() 将文件名和文件夹名拼接起来，根据系统自动加起来
class MyDataset(Dataset):
    def __init__(self, root_dir,label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, index):
        #获取其中的每一个图片
        img_name = self.img_path[index]
        #程序的相对路径
        img_item_path = os.path.join(self.root_dir, self.label_dir,img_name)
        #验证序号是否正确
        #img_path = os.listdir(path)
        #idx = 0
        #img_name = img_path[idx]  确实是第一张图片
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label




    def __len__(self):
        return len(self.img_path)
    #读取列表的长度

root_dir = "data_set/hymenoptera_data/train"
ants_label_dir = "ants"
ants_dataset = MyDataset(root_dir,ants_label_dir)

#获得第一张图片 ants_dataset[0]
# img, label = ants_dataset[0]
# img.show()

#蜜蜂的数据集
bees_label_dir = "bees"
bees_dataset = MyDataset(root_dir,bees_label_dir)

#训练数据集
train_dataset = ants_dataset +bees_dataset

#tensflow 图形的output