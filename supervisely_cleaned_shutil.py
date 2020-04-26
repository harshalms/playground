import numpy as np 
import shutil
import os


supervisely_cleaned_combo = os.listdir('/home/user/Desktop/recleaning@90%/2k/second_clean_supervisely')
combo = {}
for img in supervisely_cleaned_combo:
    name = img.split('.')
    combo[name[0]] = img

print('Size of cleaned supervisely:',len(combo)) 
# Copy Images 
img_source = os.listdir('/home/user/Desktop/supervisely/img')
path = '/home/user/Desktop/supervisely/img/'
img_destination = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/images'
img_destination = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/img2'
# Copy mat files
mask_source = os.listdir('/home/user/Desktop/recleaning@90%/2k/second_mat_mask')
mask_path = '/home/user/Desktop/recleaning@90%/2k/second_mat_mask/'
mask_destination = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/supervisely_png_mat'
mask_destination = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/mask2'
# images = {}
count=0
# for img in img_source:
#     # print(img, type(img))
#     name = img.split('.')
#     # images[name[0]] = img
#     if name[0] in combo:
#         count+=1
#         source = path + img
#         shutil.copy2(source, img_destination)

print('images done', len(mask_source))
for mask in mask_source:
    # print(img, type(img))
    print(mask)
    name = mask.split('_')
    # images[name[0]] = img
    if name[0] in combo:
        source = mask_path + mask
        print("source===>", source)
        shutil.copy2(source, mask_destination)

print('masks done')