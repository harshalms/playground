import os
import shutil

total = os.listdir('/home/user/IoTian/suervisely_uncleaned_data/combo')
print(len(total))
harshal = '/media/user/harshal/harshal'
rajib = '/media/user/harshal/rajib'
shivani = '/media/user/harshal/shivani'
mansi = '/media/user/harshal/mansi'
for i in range(len(total)):
    if i < 1000:
        source = '/home/user/IoTian/suervisely_uncleaned_data/combo/' + total[i]
        shutil.move(source, harshal)
    elif i >= 1000 and i < 2000:
        source = '/home/user/IoTian/suervisely_uncleaned_data/combo/' + total[i]
        shutil.move(source, rajib)
    elif i >= 2000 and i < 3000:
        source = '/home/user/IoTian/suervisely_uncleaned_data/combo/' + total[i]
        shutil.move(source, shivani)
    else:
        source = '/home/user/IoTian/suervisely_uncleaned_data/combo/' + total[i]
        shutil.move(source, mansi)
