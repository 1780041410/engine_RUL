#!/usr/bin/env python
# coding=utf-8
'''
    说明: 本文件的目的是将测试集合的RUL数据集按照 early 和
          later 分为两个子集合

'''

import pandas as pd
import numpy as np 

index1 = ['RUL']   
index2 = ['unit']


RUL_data = pd.read_table('RUL_FD001.txt',delim_whitespace=True,header=None,names=index1,encoding='utf-8')

early_test_X_unit_ID = pd.read_table('early_failed_testing_set.txt',delim_whitespace=True,usecols=[0],names=index2,encoding='utf-8')
early_unit_ID = set(early_test_X_unit_ID.unit)

later_test_X_unit_ID = pd.read_table('later_failed_testing_set.txt',delim_whitespace=True,usecols=[0],names=index2,encoding='utf-8') 
later_unit_ID = set(later_test_X_unit_ID.unit)  

early_RUL = []
later_RUL = []

for item in early_unit_ID:
    early_RUL.append(RUL_data.iloc[[item-1]])

for item in later_unit_ID:
    later_RUL.append(RUL_data.iloc[[item-1]]) 


early_RUL_data = pd.concat(early_RUL)
later_RUL_data = pd.concat(later_RUL)

early_RUL_data.to_csv('early_RUL_data.txt',header=False,index=False,sep=' ')
later_RUL_data.to_csv('later_RUL_data.txt',header=False,index=False,sep=' ')


#print(len(early_now_age_data))
#print(len(later_now_age_data))
#print(early_now_age_data)
#print(later_now_age_data)










