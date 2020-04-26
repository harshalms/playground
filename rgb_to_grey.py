
import matplotlib.pyplot as plt 
import cv2
import numpy as np 
from scipy.io import loadmat

def read_img(img_path, input_sz=(224, 224)):
    """
    Read image file and return cropped, resized, intensity-normalized array
        Arguments
            :img_path: str
            :crop_specs: list
            :input_sz: tuple
        Output
            :rgb_norm: numpy array
    """
    bgr = cv2.imread(img_path)
    rgb = bgr[:,:,::-1]
    # if len(crop_specs) == 4:
    #     rgb = rgb[ crop_specs[0]:crop_specs[1], crop_specs[2]:crop_specs[3], :]
    rgb = cv2.resize(rgb, (600, 800))
    rgb = cv2.resize(rgb, input_sz)
    rgb_norm = rgb.astype(np.float32)/ 255.
    
    return rgb_norm

path = '/home/user/IoTian/merge_masks/00001.jpg'
mask = read_img(path)
# mask = plt.imread('/home/user/IoTian/merge_masks/00001.jpg')
plt.imshow(mask)
# combo1 = mask[:,:,0]>0 #*img
# plt.imshow(combo1)
plt.show()
# print(combo1.shape)

combo = mask[:,:,0]>0 #*img
plt.imshow(combo.astype("uint8"))
plt.show()

mask = cv2.resize(mask, (224, 224))
mask = np.expand_dims(mask, axis=2)
cv2.imwrite('image_save_new.png', mask[:,:,0])





mask_jpg = cv2.imread('image_save_new.png')
plt.imshow(mask_jpg)
plt.show()
print(mask_jpg.shape)
mask_jpg = cv2.cvtColor(mask_jpg, cv2.COLOR_BGR2GRAY)
#print(mask.shape,mask.dtype)
print(np.max(mask_jpg))
#mask_jpg = cv2.resize(mask_jpg, (224, 224))
mask_jpg = np.expand_dims(mask_jpg, axis=2)
mask_jpg.shape

# plt.imshow(mask_jpg[:,:,0])

combo = mask_jpg[:,:,0]>0#*img
plt.imshow(combo.astype("uint8"))
plt.show()

