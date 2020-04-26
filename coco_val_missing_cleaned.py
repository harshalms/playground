import os

coco_val_cleaned_images = os.listdir('/home/user/Desktop/full_n_final/coco_val_cleaned_images')
print(len(coco_val_cleaned_images))

coco_val_cleaned_mat_masks = os.listdir('/home/user/Desktop/full_n_final/coco_val_cleaned_mat_masks')
print(len(coco_val_cleaned_mat_masks))

masks = {}
for mask in coco_val_cleaned_mat_masks:
    name = mask.split('_')
    masks[name[0]] = mask

for img in coco_val_cleaned_images:
    name = img.split('.')
    if name[0] not in masks:
        os.remove('/home/user/Desktop/full_n_final/coco_val_cleaned_images/'+img)
        # print(img)
print(len(coco_val_cleaned_images))
print(len(coco_val_cleaned_mat_masks))