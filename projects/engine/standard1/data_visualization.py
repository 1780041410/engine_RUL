#!/usr/bin/env python
# coding=utf-8
'''
  共给出两张图集：
  
  第一个图集：14张图，每一张图中是所有unit的该sensor测量值随其cycle
              的变化曲线。数据采用 min-max 标准化数据。
  
  第二个图集：14张图，每一张图中是所有unit的该sensor测量值随其cycle
              的变化曲线。数据采用 一阶差分 数据。

'''
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

#****************************************************导入标准化数据和一阶差分数据*********************************************************#
index = ['unit','cycle','s1','s2','s3','s6','s7','s8','s10','s11','s12','s13','s14','s16','s19','s20']

#standard_train_14   = pd.read_table('standard_FD001_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
first_diff_train_14 = pd.read_table('first_diff_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')


#******************************************************提取单独的列进行可视化*************************************************************#

# 提取标准化数据和差分数据对应的unit数目
#last_row_standard_train   = len(standard_train_14) - 1
last_row_first_diff_train = len(first_diff_train_14) - 1

#last_unit_standard_train   = int(standard_train_14.loc[last_row_standard_train,'unit'])     # 标准型训练数据上的unit总个数
last_unit_first_diff_train = int(first_diff_train_14.loc[last_row_first_diff_train,'unit']) # 一阶差分训练数据上的unit总个数 


#****************************************先处理标准型数据***************************************#

# 用列表存储sensor数据与对应的cycle数据

'''
pool_sensor = []
pool_cycle  = []
sensor_names = ['s1','s2','s3','s6','s7','s8','s10','s11','s12','s13','s14','s16','s19','s20']

for unit in range(last_unit_standard_train):
    temp1 = standard_train_14[standard_train_14.unit==unit] # 先提取出同一个unit的所有数据
    temp_cycle = temp1.loc[:,'cycle']   # 提取出当前unit对应的cycle的数据
    pool_cycle.append(temp_cycle)       # 将cycle数据用列表收集起来
    temp2 = temp1.loc[:,'s1']           # 提取sensor数据    
    pool_sensor.append(temp2)           # 收集sensor数据 

'''

#****************************************再处理一阶差分数据***************************************#
pool_sensor_diff = []
pool_cycle_diff  = []

for unit in range(last_unit_first_diff_train):
    temp1 = first_diff_train_14[first_diff_train_14.unit==unit]
    temp_cycle = temp1.loc[:,'cycle']
    pool_cycle_diff.append(temp_cycle)
    temp2 = temp1.loc[:,'s20']  
    pool_sensor_diff.append(temp2) 


#****************************************画图*****************************************#
# 先画标准数据sensor变化情况
'''
plt.figure(1)  
for unit in range(len(pool_cycle)):
    plt.plot(pool_cycle[unit],pool_sensor[unit])

plt.show()
'''
# 再画差分数据

'''
plt.figure(2)
for unit in range(len(pool_cycle_diff)):
    plt.plot(pool_cycle_diff[unit],pool_sensor_diff[unit])
plt.show()
'''

plt.figure()
plt.plot(pool_cycle_diff[4],pool_sensor_diff[4])
plt.show()







