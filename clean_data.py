import os
# Total images
merge_masks = os.listdir('/home/user/IoTian/merge_masks')
print(len(merge_masks))
# Flickr
cropped_images = os.listdir('/home/user/IoTian/Flicker_dataset/cropped_images')
print(len(cropped_images))
# COCO validation
data = os.listdir('/home/user/Desktop/data-20200122T062707Z-001/data')
print(len(data))

count_cropped = 0
for name in cropped_images:
    if name in merge_masks:
        os.remove('/home/user/IoTian/merge_masks/'+name)
        count_cropped+=1
print('Total cropped removed are', count_cropped)

count_coco_val = 0
for name in data:
    if name in merge_masks:
        os.remove('/home/user/IoTian/merge_masks/'+name)
        count_coco_val+=1
print('Total coco_val removed are', count_coco_val)

# Rechecking size of all folders
# Total images
merge_masks = os.listdir('/home/user/IoTian/merge_masks')
print('Total:', len(merge_masks))
# Flickr
cropped_images = os.listdir('/home/user/IoTian/Flicker_dataset/cropped_images')
print('Flickr:',len(cropped_images))
# COCO validation
data = os.listdir('/home/user/Desktop/data-20200122T062707Z-001/data')
print('coco:',len(data))