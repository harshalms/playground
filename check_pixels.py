import cv2
from scipy.io import loadmat
import matplotlib.pyplot as plt

flickr_mat = loadmat('/home/user/IoTian/Flicker_dataset/images_mask/00001_mask.mat')
flickr = flickr_mat['mask']
plt.imshow(flickr)
plt.show()

my_mat = loadmat('/home/user/IoTian/final_dataset/mat_mask/00001_mask.mat')
mat = my_mat['mask']
plt.imshow(mat)
plt.show()

perfect_mat = loadmat('/home/user/IoTian/final_mat_mask/00001_mask.mat')
per_mat = perfect_mat['mask']
plt.imshow(per_mat)
plt.show()