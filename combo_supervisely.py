import os
import numpy as np
import cv2
import matplotlib.pyplot as plt 
import random 

list_img = os.listdir('/home/user/Desktop/supervisely/img')
print('length list_img:',len(list_img))
img_dict = {}
for img in list_img:
    name = img.split('.')
    img_dict[name[0]] = img
print('length img_dict:',len(img_dict))

list_mask = os.listdir('/home/user/Desktop/supervisely/machine_mask')
print('length list_mask:',len(list_mask))
mask_dict = {}
for mask in list_mask:
    name = mask.split('.')
    mask_dict[name[0]] = mask
print('length mask_dict:',len(mask_dict))
print()
print()
# checking if img_dict and mask_dict has same keys for related masks and images
# print(type(img_dict.keys()))
random_key = random.sample(img_dict.keys(), 1)[0]
print(img_dict[random_key], mask_dict[random_key])
# print(type(random_key), type(mask_dict[random_key]))

# Generating all the combos
count = 0
for mask in mask_dict.keys():
    mask_path = '/home/user/Desktop/supervisely/machine_mask/' + mask_dict[mask]
    mask_matrix = cv2.imread(mask_path)
    mask_matrix = mask_matrix//np.amax(mask_matrix)
    # print(type(mask_matrix))
    img_path = '/home/user/Desktop/supervisely/img/' + img_dict[mask]
    img_matrix = cv2.imread(img_path)
    combo = img_matrix*mask_matrix
    # combo = combo[:,:,::-1]
    combo_path = '/home/user/Desktop/supervisely/combo/' + mask + '.png'
    cv2.imwrite(combo_path, combo)
    count+=1
    if count%50==0:
        print('{} images are written successfully'.format(count))
print('{} images are written successfully'.format(count))
