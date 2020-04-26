import scipy.io as sio
import numpy as np 
import cv2
import os

MBO_mask = os.listdir('/home/user/Desktop/full_n_final/MBO_img_mask')
print(len(MBO_mask))

try: 
    # creating a folder named data 
    if not os.path.exists('/home/user/Desktop/full_n_final/MBO_mat_masks'): 
        os.makedirs('/home/user/Desktop/full_n_final/MBO_mat_masks') 

# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of MBO_mat_masks')

count = 0
for mask in MBO_mask:
    path = '/home/user/Desktop/full_n_final/MBO_img_mask/' + mask
    mask_matrix = cv2.imread(path)
    mask_matrix = mask_matrix[:,:,::-1]
    mask_matrix = mask_matrix//np.amax(mask_matrix)
    mask_matrix = mask_matrix[:,:,0]
    id = mask.split('.')
    sio.savemat('/home/user/Desktop/full_n_final/MBO_mat_masks/'+str(id[0])+'_mask'+'.mat', {'mask':mask_matrix})
    count+=1
    if count%50==0:
        print('{} .mat files download'.format(count))

print('{} .mat files download'.format(count))