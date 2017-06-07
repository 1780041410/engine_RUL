#!/usr/bin/env python
# coding=utf-8
'''
    说明: 本文件的目的是将测试集合的now_age数据集按照 early 和
          later 分为两个子集合

'''

import pandas as pd
import numpy as np 

index1 = ['age']
index2 = ['unit']


now_age_data = pd.read_table('now_age_FD001.txt',delim_whitespace=True,header=None,names=index1,encoding='utf-8')
#print(now_age_data)
#INPUT = input()  

early_test_X_unit_ID = pd.read_table('early_failed_test.txt',delim_whitespace=True,usecols=[0],names=index2,encoding='utf-8')
early_unit_ID = set(early_test_X_unit_ID.unit)

later_test_X_unit_ID = pd.read_table('later_failed_test.txt',delim_whitespace=True,usecols=[0],names=index2,encoding='utf-8') 
later_unit_ID = set(later_test_X_unit_ID.unit)  

early_now_age = []
later_now_age = []

for item in early_unit_ID:
    early_now_age.append(now_age_data.iloc[[item-1]])

for item in later_unit_ID:
    later_now_age.append(now_age_data.iloc[[item-1]]) 


early_now_age_data = pd.concat(early_now_age)
later_now_age_data = pd.concat(later_now_age)

early_now_age_data.to_csv('early_now_age_data.txt',header=False,index=False,sep=' ')
later_now_age_data.to_csv('later_now_age_data.txt',header=False,index=False,sep=' ')


#print(len(early_now_age_data))
#print(len(later_now_age_data))
#print(early_now_age_data)
#print(later_now_age_data)










