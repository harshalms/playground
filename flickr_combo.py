import os
import numpy as np
import cv2
import matplotlib.pyplot as plt 
import random 
from scipy.io import loadmat

list_img = os.listdir('/home/user/IoTian/Flicker_dataset/cropped_images')
print('length list_img:',len(list_img))
img_dict = {}
for img in list_img:
    name = img.split('.')
    img_dict[name[0]] = img
print('length img_dict:',len(img_dict))
print()

list_mask = os.listdir('/home/user/IoTian/Flicker_dataset/images_mask')
print('length list_mask:',len(list_mask))
mask_dict = {}
for mask in list_mask:
    name = mask.split('_')
    mask_dict[name[0]] = mask
print('length mask_dict:',len(mask_dict))
print()

count = 0
for mask in mask_dict.keys():
    mask_path = '/home/user/IoTian/Flicker_dataset/images_mask/' + mask_dict[mask]
    mat = loadmat(mask_path)
    mask_matrix = mat['mask']
    # mask_matrix = mask_matrix//np.amax(mask_matrix)
    mask_matrix = np.expand_dims(mask_matrix, axis=2)
    # print(type(mask_matrix))
    if mask not in img_dict.keys():
        continue
    else:
        img_path = '/home/user/IoTian/Flicker_dataset/cropped_images/' + img_dict[mask]
        img_matrix = cv2.imread(img_path)
        img_matrix = cv2.resize(img_matrix, (600, 800))
        # img_matrix = img_matrix[:,:,::-1]
        if img_matrix is None:
            continue
        # print(img_matrix.shape, mask_matrix.shape)
        combo = img_matrix*mask_matrix
    #   combo = combo[:,:,::-1]
        combo_path = '/home/user/IoTian/Flicker_dataset/flickr_combo/' + mask + '.png'
        cv2.imwrite(combo_path, combo)
        count+=1
    if count%50==0:
        print('{} images are written successfully'.format(count))
print('{} images are written successfully'.format(count))
