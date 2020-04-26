import numpy as np 
import shutil
import os


coco_val_cleaned_mask = os.listdir('/home/user/Desktop/recleaning@90%/4k/coco_combo')
cleaned_mask = {}
for img in coco_val_cleaned_mask:
    name = img.split('.')
    cleaned_mask[name[0]] = img

print('Size of cleaned coco_val:',len(cleaned_mask)) 

img_source = os.listdir('/home/user/IoTian/final_dataset/images')
path = '/home/user/IoTian/final_dataset/images/'
img_destination = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/images'

mask_source = os.listdir('/home/user/Desktop/full_n_final/coco_val_cleaned_mat_masks')
mask_path = '/home/user/Desktop/full_n_final/coco_val_cleaned_mat_masks/'
mask_destination = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/mat_masks'
# images = {}
for img in img_source:
    # print(img, type(img))
    name = img.split('.')
    # images[name[0]] = img
    if name[0] in cleaned_mask:
        source = path + img
        shutil.copy2(source, img_destination)
print('images done')
count = 0
some = 0
for mask in mask_source:
    # print(img, type(img))
    name = mask.split('_')
    # images[name[0]] = img
    if name[0] in cleaned_mask:
        count+=1
        source = mask_path + mask
        shutil.copy2(source, mask_destination)
    
print(count)
print(some)
print('masks done')