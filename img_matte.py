# from utils.rawdata_prep import *
from scipy.io import loadmat
import matplotlib.pyplot as plt
import random
import cv2
from random import shuffle
import numpy as np

def read_mask_mat(mat_fname, mask_sz):
    """
    extract mask as a binary image array
        :mat_fname: str
        :mask_sz: tuple
    """
    print(mat_fname)
    mat = loadmat(mat_fname)
    mask = mat["mask"]
    mask = mask.astype( np.float32 )
    mask_rsz = cv2.resize(mask, mask_sz)
    mask_rsz = np.expand_dims(mask_rsz, axis=2)
    # print(mask_rsz.shape)
    return mask_rsz


def read_image_file(img_fname, crop, img_input_sz):
    """
    read raw image, resize and output array
    """
    bgr = cv2.imread( img_fname )
    rgb = bgr[:, :, ::-1]
    # if np.sum(crop) != 0: #image must be cropped
    #     assert len(crop)==4, "crop specs list must be of length 4"
    #     yi, yf, xi, xf = crop
    #     rgb = rgb[yi:yf, xi:xf, :]
    
    rgb_rsz = cv2.resize(rgb, (600, 800))
    img_rsz = cv2.resize(rgb_rsz, img_input_sz)
    # print(img_rsz.shape)
    return img_rsz

num = '/home/user/IoTian/final_dataset/images/000000279929.jpg'
fname = '/home/user/IoTian/final_dataset/mat_mask/000000279929_mask.mat'


mask = read_mask_mat(fname, mask_sz=(224,224))
img = read_image_file(num, crop= 'None', img_input_sz=(224,224))
combo = mask*img
# plt.imshow(img)
plt.imshow(mask[:,:,0]>0.267)
# plt.imshow(combo.astype("uint8"))
plt.show()