#!/usr/bin/env python
# coding=utf-8
'''
    说明：本文件的目的是将训练数据集的标签数据
          也即RUL数据进行120的常数处理,具体做法：
          将每个unit的前20个cycle的RUL置为120
    结果：写出到文件,只将RUL数据写出到文件     
'''

import pandas as pd  
#×××××××××××××××××××××××××××××××××××××××××× 读入数据 ××××××××××××××××××××××××××××××××××××××#
index = ['unit','cycle','RUL'] 
extended_RUL = pd.read_table('extended_RUL_with_unit_cycle_ID_FD001.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8') 

#×××××××××××××××××××××××××××× 将每个unit的前20个cycle的RUL设为20 ××××××××××××××××××××××××××××××××××××××#

last_row = len(extended_RUL) - 1
last_unit = int(extended_RUL.loc[last_row,'unit'])
constant_value = pd.DataFrame([120]*20) 
result_RUL = []

for unit in range(1,last_unit+1):
    slice_unit = extended_RUL[extended_RUL.unit==unit]
    slice_RUL  = slice_unit.loc[:,'RUL']
    temp1 = pd.concat([constant_value,slice_RUL[20:]],ignore_index=True)   
    result_RUL.append(temp1)  

result_RUL = pd.concat(result_RUL,axis=0)   
result_RUL.to_csv('extended_RUL_no_unit_cycle_ID_FD001.txt',header=False,index=False,sep=' ')



