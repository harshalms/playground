# importing required modules 
from zipfile import ZipFile 

# specifying the zip file name 
# file_name = 
file_name = ["/home/user/Downloads/level_3_train.zip", "/home/user/Downloads/level_3_test.zip"]
for file in file_name:
    # opening the zip file in READ mode 
    with ZipFile(file, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 

        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall('/home/user/playground/zip_extract') 
        print('Done!') 
