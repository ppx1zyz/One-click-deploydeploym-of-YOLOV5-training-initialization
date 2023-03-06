import os
import random
yoloPath='yolov5-master'
trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = yoloPath+'/data/Annotations'
txtsavepath = yoloPath+'/data/ImageSets'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open(yoloPath+'/data/ImageSets/trainval.txt', 'w')
ftest = open(yoloPath+'/data/ImageSets/test.txt', 'w')
ftrain = open(yoloPath+'/data/ImageSets/train.txt', 'w')
fval = open(yoloPath+'/data/ImageSets/val.txt', 'w')
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
