import os
import shutil
# copy data from old_mask_dir which is similar to data in new_mask_dir
old_mask_dir = os.listdir('path/to/the/old_mask_dir')
new_mask_dir = os.listdir('path/to/the/new_mask_dir')

try: 
    # creating a folder named copied_mask_data. This is destination directory.
    if not os.path.exists('~/Desktop/copied_mask_data'): 
        os.makedirs('~/Desktop/copied_mask_data') 

# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of second_mat_mask')

destination = '~/Desktop/copied_mask_data'
for mask in new_mask_dir:
    if mask in old_mask_dir:
        source = 'path/to/the/old_mask_dir/' + mask
        shutil.copy2(source, destination)
