#!/usr/bin/env python
# coding=utf-8
'''
说明：
    根据14个候选特征构建3个新的特征
    分别为：
    feature_in:  2, 3, 4, 8, 11, 13, 15, 17
    feature_de:  7, 12, 20, 21
    feature_mix: 9, 14 

注意：
    这里在导入文件时,sensor们从1开始编号

结果：
    最后将三个特征写出到一个文件，前两列带有unit和cycle的
    ID号
'''
import pandas as pd

#*******************************************************************************读入文件**************************#
index = ['unit','cycle','s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']
index_unit_cycle = ['unit','cycle'] 
index_in  = ['s2','s3','s4','s8','s11','s13','s15','s17'] 
index_de  = ['s7','s12','s20','s21']
index_mix = ['s9','s14']
standard_14 = pd.read_table('standard_FD001_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')

#*******************************************************************************分割文件**************************#
unit_cycle_ID = standard_14.loc[:,index_unit_cycle]  
standard_in   = standard_14.loc[:,index_in]  
standard_de   = standard_14.loc[:,index_de]
standard_mix  = standard_14.loc[:,index_mix]

#******************************************************************************计算权重向量***********************#
#******************计算每一列的方差****************#
# 这里的方差默认是用 N-1 正规化过的
var_in  = standard_in.var()
var_de  = standard_de.var()
var_mix = standard_mix.var()

#**************基于方差计算每一列的权重向量*************#
# 转换为列表以方便使用列表解析的方式
varSum_in,varSum_de,varSum_mix = var_in.sum(),var_de.sum(),var_mix.sum() 

var_in  = var_in.tolist()
var_de  = var_de.tolist()
var_mix = var_mix.tolist()

weights_in  = [x/float(varSum_in) for x in var_in]
weights_de  = [y/float(varSum_de) for y in var_de]
weights_mix = [z/float(varSum_mix) for z in var_mix]

#******************************************************************************计算新的三个特征*****************#
sensor_in  = [standard_in.s2,standard_in.s3,standard_in.s4,standard_in.s8,
              standard_in.s11,standard_in.s13,standard_in.s15,standard_in.s17] 
sensor_de  = [standard_de.s7,standard_de.s12,standard_de.s20,standard_de.s21]
sensor_mix = [standard_mix.s9,standard_mix.s14]

feature_in  = sum([sensor*weight for sensor,weight in zip(sensor_in,weights_in)])
feature_de  = sum([sensor*weight for sensor,weight in zip(sensor_de,weights_de)])
feature_mix = sum([sensor*weight for sensor,weight in zip(sensor_mix,weights_mix)])

#*****************************************************************************组合三个特征并写出到文件***********#
feature_vector = [unit_cycle_ID,feature_in,feature_de,feature_mix]
feature_vector = pd.concat(feature_vector,axis=1)
feature_vector.to_csv('new_features_3_train.txt',index=False,header=False,sep=' ')

print(weights_in)
print(weights_de)
print(weights_mix)

















































