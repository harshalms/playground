import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import os

img_dir = os.listdir('/home/user/IoTian/Rajib_data/random_bg/original_images')
mask_dir = os.listdir('/home/user/IoTian/Rajib_data/random_bg/original_masks')
bg_dir = os.listdir('/home/user/IoTian/Rajib_data/random_bg/bgs')

for im in img_dir:
    img_path = '/home/user/IoTian/Rajib_data/MBO_img/' + im
    img = cv2.imread(img_path)
    mask_name = im.split('.')
    mask_path = '/home/user/IoTian/Rajib_data/MBO_img_mask/' + mask_name[0] + '.png'
    mask = cv2.imread(mask_path)
    bkg = cv2.imread('/home/user/IoTian/Rajib_data/random_bg/bgs/ubuntu.jpg')
    shape = img.shape
    print('shape', shape)
    bkg_resize = cv2.resize(bkg, (shape[1], shape[0]))
    print(bkg_resize.shape)
# flip_mask = 255-mask
# flip_mask = flip_mask//255
# create_bkg = bkg_resize*flip_mask
    normalized_mask = mask//np.amax(mask)
    combo = img*normalized_mask
    combo1 = combo>0
    combo1 = combo1.astype('int')
    combo1[combo1==1]=255
    combo1 = 255 - combo1
    combo1 = combo1//255
    create_bkg = bkg_resize*combo1
    add_bkg = create_bkg + combo
    name = '/home/user/IoTian/Rajib_data/random_bg/output/' + mask_name[0] + '_' + 'ubuntu.png'
    cv2.imwrite(name, add_bkg)
    add_bkg=add_bkg[:,:,::-1]
    combo=combo[:,:,::-1]
    # plt.imshow(combo)
    # plt.show()