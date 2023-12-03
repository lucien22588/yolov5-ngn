import os
import random


random.seed(101)

path_root = '/workspace/Ww/V5_DRONE/DRONE_DATA'  # 修改为自己

trainval_percent = 1
train_percent = 0.7
imgfilepath = path_root + '/labels'
total_img = os.listdir(imgfilepath)

num = len(total_img)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrain = open(path_root + '/train.txt', 'w')
fval = open(path_root + '/val.txt', 'w')

for i in list:
    name = imgfilepath.replace('labels', 'images') + '/' + total_img[i]
    name = name.replace('txt', 'jpg') + '\n'
    if i in trainval:
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)

ftrain.close()
fval.close()
