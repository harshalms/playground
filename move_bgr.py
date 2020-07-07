import os
import shutil

def move(bgr, img):
    bgr = os.listdir(bgr)
    img_list = os.listdir(img)
    bgr_dict = []
    for i in bgr:
        bgr_dict.append(i.split('.')[0]+'.png')
    
    if not os.path.exists('./videoplayback_moved'):
        os.makedirs('videoplayback_moved')
    
    for image in img_list:
        if image in bgr_dict:
            shutil.move(img+'/'+image, '/home/user/playground/videoplayback_moved') 

    return bgr_dict


if __name__ == "__main__":
    bgr = '/home/user/Downloads/drive-download-20200522T084538Z-001/videoplayback_bgr'
    img = '/home/user/Downloads/drive-download-20200522T084538Z-001/videoplayback'
    
    (move(bgr, img))
