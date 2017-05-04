#!/usr/bin/env python2


'''
%该代码根据已生成的xml，制作VOC2007数据集中的trainval.txt;train.txt;test.txt和val.txt  
%trainval占总数据集的80%，test占总数据集的80%；train占trainval的80%，val占trainval的20%；  
%上面所占百分比可根据自己的数据集修改，如果数据集比较少，test和val可少一些  
'''

import random
import os
import pandas as pd

# 设置比率
trainval_ratio = 0.8
test_ratio= 0.2
train_ratio = 0.8
val_ratio = 0.2

# 批量获得图像ID
root_dir = '/data/DeepLearningForTraining/UMDFaces/VOC2007/JPEGImages'
file_list = os.listdir(root_dir)

# 随机抽样
# 核心思想：索引的随机抽样，这样非常方便
trainval_item = random.sample(range(0,len(file_list)),int(len(file_list)*trainval_ratio)) 
test_item = set(range(0,len(file_list))) - set(trainval_item)
train_item = random.sample(trainval_item,int(len(trainval_item)*train_ratio)) 
val_item = random.sample(test_item,int(len(trainval_item)*val_ratio)) 

# 所有的图像ID
face_id = []
for f in file_list:
    face_id.append(os.path.splitext(f)[0])

# 根据trainval索引的图像ID
trainval_id = []
for i in trainval_item:
    trainval_id.append(face_id[i])

# 根据test索引的图像ID
test_id = []
for i in test_item:
    test_id.append(face_id[i])

# 根据test索引的图像ID
train_id = []
for i in train_item:
    train_id.append(face_id[i])

# 根据test索引的图像ID
val_id = []
for i in val_item:
    val_id.append(face_id[i])

# 保存为txt，ImageSets
save_dir = '/data/DeepLearningForTraining/UMDFaces/VOC2007/ImageSets/'
# pd.Series(face_id).to_csv(save_dir+'face_id.txt',index = False)
pd.Series(trainval_id).to_csv(save_dir+'trainval.txt',index = False)
pd.Series(test_id).to_csv(save_dir+'test.txt',index = False)
pd.Series(train_id).to_csv(save_dir+'train.txt',index = False)
pd.Series(val_id).to_csv(save_dir+'val.txt',index = False)