import numpy as np 
import shutil
import os

flickr_combo = os.listdir('/home/user/Desktop/recleaning@90%/4k/flickr_combo')
combo = {}
for img in flickr_combo:
    name = img.split('.')
    combo[name[0]] = img

print(len(combo)) 

img_source = os.listdir('/home/user/IoTian/Flicker_dataset/cropped_images/')
path = '/home/user/IoTian/Flicker_dataset/cropped_images/'
img_destination = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/images'
mask_source = os.listdir('/home/user/Desktop/full_n_final/flickr_cleaned_masks')
mask_path = '/home/user/Desktop/full_n_final/flickr_cleaned_masks/'
mask_destination = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/flickr_mat'
# images = {}
for img in img_source:
    # print(img, type(img))
    name = img.split('.')
    # images[name[0]] = img
    if name[0] in combo:
        source = path + img
        shutil.copy2(source, img_destination)
print()
for mask in mask_source:
    # print(img, type(img))
    name = mask.split('_')
    # images[name[0]] = img
    if name[0] in combo:
        source = mask_path + mask
        shutil.copy2(source, mask_destination)


