# fp = open('/home/user/Downloads/crop.txt', 'r')
# print(fp)
import re
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

list_img = os.listdir('/home/user/IoTian/Flicker_dataset/images')
print('len===>',len(list_img))
with open("/home/user/Downloads/crop.txt", 'rb') as handle:
    # print(handle)
    # line = f.next() #handle.readline()
    for line in handle.readlines():
        line1 = line.decode("utf-8")
        # print("====>", line)
        # print(type(line))
        string = re.split(' ,  |\n', line1)
        # string = str(string[0])
        # print(string[0])
        string = string[0]
        s = string.split(' ')
        # print(s[0])
        # for i in s:
        #     print(i)
        # print(s[1:])
        # name of the file
        name = s[0]
        # print(name, type(name))
        
        # cropping specifications of the file
        crop = [int(i) for i in s[1:]]
        # import pdb;pdb.set_trace()
        if name in list_img:
            path = '/home/user/IoTian/Flicker_dataset/images/' + name
            print(path)
            rgb = cv2.imread(path)
            if rgb is None:
                continue
            # print(bgr)
            # plt.imshow(bgr)
            # plt.show()
            # rgb = bgr[:, :, ::-1]
            # import pdb;
            # pdb.set_trace()
            if sum(crop) != 0: #image must be cropped
                assert len(crop)==4, "crop specs list must be of length 4"
                yi, yf, xi, xf = crop
                rgb = rgb[yi:yf, xi:xf, :]
                # new_path = '/home/user/IoTian/Flicker_dataset/cropped_images/' + name
                new_path = '/home/user/IoTian/data/images/' + name
                print(name, new_path)
                cv2.imwrite(new_path, rgb)
        # print(crop)
        # break
        
