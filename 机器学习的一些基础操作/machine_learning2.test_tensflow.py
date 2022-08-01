from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image



#crtl + 鼠标 看看怎么用

#打开tensflow的方法
#PS D:\python 程序> cd C:\Users\Lenovo\anaconda3\envs\your_env_name
#PS C:\Users\Lenovo\anaconda3\envs\your_env_name> tensorboard --logdir=
#转到安装pytorch的包的地方打开logs 文件。 因为生成的logs软件在D盘下。
# 然后编译器在C盘 应该复制文件到C盘 your_env_name
#TensorBoard 2.9.1 at http://localhost:6006/ 可以指定个端口
# tensorboard --logdir=logs --port=6007
#for i in range(100):
#    writer.add_scalar('y=2x', 2*i, i)
#从 terminal 给的地址点进去



#直接相对路径
#open cv 读取的numpy 型
writer = SummaryWriter('logs')
image_path="data_1/train/ants/0013035.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
writer.add_image("test" , img_array , 1,dataformats='HWC')
for i in range(100):
  writer.add_scalar('y=2x', 2*i, i)



writer.close()