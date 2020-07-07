import matplotlib.pyplot as plt 
import cv2
import numpy as np
import os

dir = os.listdir('../path_of_remove.bg_output/')
input_path = '../path_of_remove.bg_output/'
print(len(dir))

if not os.path.exists('../mask_folder'):    # create mask_folder  
    os.makedirs('../mask_folder')

mask_path = '../mask_folder/'               # ouput folder path to save generated mask

count = 0
for image in dir:
    img = cv2.imread(input_path+image)
    img[img>0]=255
    # img//=255                             # To normalize the images
    cv2.imwrite(mask_path+image, img)
    count+=1
    # plt.imshow(img)
    # plt.show()
    if count%50==0:
        print(count, 'files are written successfully')
print(count, 'files are written successfully')

# Finally check if all mask files are generated at mask_path
