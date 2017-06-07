#!/usr/bin/env python
# coding=utf-8
'''
    说明: 本文件的目的是给训练标签数据集前面加上两列,
          分别为unit和cycle的ID号.
    结果: 写出到文件,避免以后使用时重复处理

'''
import pandas as pd

train_FD001   = pd.read_table('train_FD001.txt',delim_whitespace=True,header=None,names=None,encoding='utf-8')
train_y_FD001 = pd.read_table('train_y_FD001.txt',delim_whitespace=True,header=None,names=None,encoding='utf-8')

unit_ID  = train_FD001[0]
cycle_ID = train_FD001[1]    
result = [unit_ID,cycle_ID,train_y_FD001]
final = pd.concat(result,axis=1)

final.to_csv('train_y_FD001_with_ID.txt',header=False,index=False,sep=' ')

