#!/usr/bin/env python
# coding=utf-8
'''
    说明: 本文件的目的是计算实际上的测试集中每个unit的总寿命,
          然后和预测的总寿命进行对比,计算误差.

'''
import pandas as pd
index_age = ['age']  
index_rul = ['rul']
now_age_FD001 = pd.read_table('now_age_FD001.txt',delim_whitespace=True,header=None,names=index_age,encoding='utf-8')
real_rul = pd.read_table('RUL_FD001.txt',delim_whitespace=True,header=None,names=index_rul,encoding='utf-8') 

real_total_life = now_age_FD001.age + real_rul.rul

real_total_life.to_csv('real_total_life.txt',header=False,index=False,sep=' ')   
