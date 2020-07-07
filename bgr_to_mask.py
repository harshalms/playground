import matplotlib.pyplot as plt 
import cv2
import numpy as np
import os

dir = os.listdir('/home/user/Downloads/cleaned_new_manual_data-20200615T053130Z-001/cleaned_new_manual_data/bgr_data/output')
print(len(dir))

if not os.path.exists('/home/user/Downloads/cleaned_new_manual_data-20200615T053130Z-001/cleaned_new_manual_data/bgr_data/mask'):
    os.makedirs('/home/user/Downloads/cleaned_new_manual_data-20200615T053130Z-001/cleaned_new_manual_data/bgr_data/mask')

path = '/home/user/Downloads/cleaned_new_manual_data-20200615T053130Z-001/cleaned_new_manual_data/bgr_data/output/'
mask_path = '/home/user/Downloads/cleaned_new_manual_data-20200615T053130Z-001/cleaned_new_manual_data/bgr_data/mask/'
count = 0
for image in dir:
    img = cv2.imread(path+image)
    img[img>0]=255
    # img//=255                         # To normalize the images
    cv2.imwrite(mask_path+image, img)
    count+=1
    # plt.imshow(img)
    # plt.show()
    if count%50==0:
        print(count, 'files are written successfully')
print(count, 'files are written successfully')
