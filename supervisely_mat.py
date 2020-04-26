import scipy.io as sio
import numpy as np 
import cv2
import os

supervisely_mask = os.listdir('/home/user/Desktop/recleaning@90%/3rd_filter_90%/supervisely_png')
print(len(supervisely_mask))

try: 
    # creating a folder named data 
    if not os.path.exists('/home/user/Desktop/recleaning@90%/3rd_filter_90%/supervisely_png_mat'): 
        os.makedirs('/home/user/Desktop/recleaning@90%/3rd_filter_90%/supervisely_png_mat') 

# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of second_mat_mask')

count = 0
for mask in supervisely_mask:
    path = '/home/user/Desktop/recleaning@90%/3rd_filter_90%/supervisely_png/' + mask
    mask_matrix = cv2.imread(path)
    mask_matrix = mask_matrix[:,:,::-1]
    mask_matrix = mask_matrix//np.amax(mask_matrix)
    mask_matrix = mask_matrix[:,:,0]
    id = mask.split('.')
    sio.savemat('/home/user/Desktop/recleaning@90%/3rd_filter_90%/supervisely_png_mat/'+str(id[0])+'_mask'+'.mat', {'mask':mask_matrix})
    count+=1
    if count%50==0:
        print('{} .mat files download'.format(count))

print('{} .mat files download'.format(count))