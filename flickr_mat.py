import scipy.io as sio
import numpy as np 
import cv2
import os

flickr_mask = os.listdir('/home/user/IoTian/Flicker_dataset/masks')
print(len(flickr_mask))

try: 
    # creating a folder named data 
    if not os.path.exists('/home/user/IoTian/Flicker_dataset/new_mat_masks'): 
        os.makedirs('/home/user/IoTian/Flicker_dataset/new_mat_masks') 

# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of second_mat_mask')

count = 0
for mask in flickr_mask:
    path = '/home/user/IoTian/Flicker_dataset/masks/' + mask
    mask_matrix = cv2.imread(path)
    mask_matrix = mask_matrix[:,:,::-1]
    mask_matrix = mask_matrix//np.amax(mask_matrix)
    mask_matrix = mask_matrix[:,:,0]
    id = mask.split('.')
    sio.savemat('/home/user/IoTian/Flicker_dataset/new_mat_masks/'+str(id[0])+'_mask'+'.mat', {'mask':mask_matrix})
    count+=1
    if count%50==0:
        print('{} .mat files download'.format(count))

print('{} .mat files download'.format(count))