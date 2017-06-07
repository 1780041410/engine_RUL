#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import numpy as np   
'''
    说明：本文件的目的是计算数据的一节差分数据,基于3个构造的新特征.

'''

def load_data():
    
    index   = ['s0','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s16','s17','s18','s19','s20']
    index1  = ['s1','s2','s3','s6','s7','s8','s10','s11','s12','s13','s14','s16','s19','s20']
    
    sensor_data_train = pd.read_table('FD001/train_X_FD001.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
    sensor_data_train_14 = sensor_data_train.loc[:,index1]  # 提取14个测量指标 
    sensor_data_train_14 = sensor_data_train_14.apply(lambda x:(x-np.min(x))/(np.max(x)-np.min(x))) #将数据标准化 
    first_difference_train_14 = sensor_data_train_14.diff()

    
    

    sensor_data_test = pd.read_table('FD001/test_X_FD001.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
    sensor_data_test_14 = sensor_data_test.loc[:,index1]
    sensor_data_test_14 = sensor_data_test_14.apply(lambda x:(x-np.min(x))/(np.max(x)-np.min(x)))
    first_difference_test_14 = sensor_data_test_14.diff()




    #train_y = pd.read_table('FD001/train_y_FD001.txt',delim_whitespace=True,header=None,encoding='utf-8')

    #test_y = pd.read_table('FD001/test_y_FD001.txt',delim_whitespace=True,header=None,encoding='utf-8')
    
    #now_age = pd.read_table('FD001/now_age_FD001.txt',delim_whitespace=True,header=None,encoding='utf-8')
    
    #RUL = pd.read_table('FD001/RUL_FD001.txt',delim_whitespace=True,header=None,encoding='utf-8')
    
    
    return first_difference_train_14,first_difference_test_14

    


if __name__ == '__main__':
    f1,f2 = load_data()
    print(f1[0:5])
    print(f2[0:5])






