import cv2
import numpy as np
import os
from scipy.io import loadmat
import matplotlib.pyplot as plt

image_list = os.listdir('/home/user/Desktop/recleaning@90%/3rd_filter_90%/images')
mask_list = os.listdir('/home/user/Desktop/recleaning@90%/3rd_filter_90%/mat_masks')
pair_list = os.listdir('/home/user/Desktop/recleaning@90%/4th_filter/img_mask')
img_path = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/images/'
mask_path = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/mat_masks/'

count = 0
for img in image_list:
    # print(type(img))
    mat_name = img.split('.')
    pair = mat_name[0]+'.png'
    if pair in pair_list:
        
        mask = mat_name[0]+'_mask.mat'
        if mask in mask_list:
            fig, ax = plt.subplots(1, 3)
            mat = loadmat(mask_path+mask)
            mask = mat['mask']
            mask_shape = mask.shape
            mask_expand = np.expand_dims(mask, axis=2)
            # print(type(mask))
            img_mat = cv2.imread(img_path+img)
            img_resize = cv2.resize(img_mat, (mask_shape[1], mask_shape[0]))
            combo = img_resize*mask_expand
            combo = combo[:,:,::-1]
            img_mat = img_mat[:,:,::-1]
            # print(type(img_mat))
            
            ax[0].imshow(img_mat) #row=0, col=0
            ax[1].imshow(mask, cmap="gray") #row=0, col=1
            ax[2].imshow(combo)
            # fig.show()
            
            path = '/home/user/Desktop/recleaning@90%/4th_filter/img_mask/' + mat_name[0] + '.png'
            fig.savefig(path)
            plt.close()
            count+=1
        if count%50==0:
            print(count, 'pairs are written')
print(count, 'pairs are written')
