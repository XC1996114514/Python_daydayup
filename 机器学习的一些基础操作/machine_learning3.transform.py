from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from PIL import Image
img_path = "data_set/hymenoptera_data/train/ants/5650366_e22b7e1065.jpg"
img = Image.open(img_path)

write=SummaryWriter("logs")

tensor_trans= transforms.ToTensor()
tensor_img = tensor_trans(img )
write.add_image("Tensor_img",tensor_img)

write.close()

