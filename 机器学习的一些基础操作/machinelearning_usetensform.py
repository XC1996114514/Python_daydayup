from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
writer = SummaryWriter("logs")
img = Image.open('image/00307.jpg')
print(img)


#totensor 的使用
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("Totensor",img_tensor)


#Normalize
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm = trans_norm(img_tensor)
print(img_norm[0][0][0])
writer.add_image("normal",img_norm,1)
writer.close()

#Resize
print(img.size)
trans_resize = transforms.Resize((512,512))
# img pil -> resize ->img_resize pil
img_resize = trans_resize(img)
# img resize -> totensor - >img_resize tensor
img_resize = trans_totensor(img_resize)
writer.add_image("Resize",img_resize,0)
print(img_resize)

#转到编译器目录下的terminal运行文件

#Random cut
#需要裁剪一个500*1000
trans_random = transforms.RandomCrop(500,1000)
trans_compose_2 = transforms.Compose([trans_random,trans_totensor])
for i in range(10):
    img_crop = trans_compose_2(img)
    writer.add_image("RandomCrop",img_crop,i)