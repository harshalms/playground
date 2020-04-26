import numpy as np 
import matplotlib.pyplot as plt 
import cv2

img = cv2.imread('/home/user/Desktop/second_img/adult-beautiful-beauty-face-41191.png')
mask = cv2.imread('/home/user/Desktop/second_mask/adult-beautiful-beauty-face-41191.png')
bkg = cv2.imread('/home/user/Desktop/bkg.jpg')
print(np.amax(bkg))
bkg = cv2.resize(bkg, (533, 800))
bkg = bkg.astype('float32')/255

mask = mask// np.amax(mask)
rev_mask = abs(mask - 1)
print(img.shape, bkg.shape)
print(img.dtype, bkg.dtype)

bkg_matted = bkg*rev_mask
mixed = img*mask
combo = (mixed+bkg_matted)/2

mixed=mixed[:,:,::-1]
plt.imshow(mixed)
plt.show()
combo=combo[:,:,::-1]
plt.imshow(combo)
plt.show()