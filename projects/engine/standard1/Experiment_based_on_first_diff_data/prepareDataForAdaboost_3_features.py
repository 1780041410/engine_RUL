#!/usr/bin/env python
# coding=utf-8
'''
    说明： 载入数据,传给Adaboost regression 
    特征： 14个sensor数据的一阶差分数据,计数从2开始.

    train_X  | 20630 
    train_y  | 20630   
    test_X   | 13095   

'''
import pandas as pd 
import numpy as np 

def prepareData():
    index   = ['unit','cycle','feature_in','feature_de','feature_mix']
    index_f = ['feature_in','feature_de','feature_mix']
    index_c = ['cycle'] 
    
    train_X_temp  = pd.read_table('extended_tail_data_train_X_FD001.txt',delim_whitespace=True,
                                          header=None,names=index,encoding='utf-8')

    test_X_temp   = pd.read_table('test_100_X_3_features_FD001.txt',delim_whitespace=True,
                                          header=None,names=index,encoding='utf-8')

    train_y_temp  = pd.read_table('extended_RUL_no_unit_cycle_ID_FD001.txt',delim_whitespace=True,header=None,names=index_c,encoding='utf-8')

    real_RUL_temp = pd.read_table('RUL_FD001.txt',delim_whitespace=True,header=None,names=index_c,encoding='utf-8') 
   
    # 训练数据
    train_X  = train_X_temp.loc[:,index_f] 
    train_X  = train_X.as_matrix()  # train_X

    train_y  = train_y_temp.cycle.tolist()
    train_y  = np.array(train_y)    # train_y  
    
    # 预测数据 
    test_X   = test_X_temp.loc[:,index_f]
    test_X   = test_X.as_matrix()   # test_X  
    
    real_RUL = real_RUL_temp.cycle.tolist()
    real_RUL = np.array(real_RUL)   # real_RUL  
    
    return train_X, train_y, test_X, real_RUL   




# 函数测试

if __name__ == '__main__':
    train_X,train_y,test_X,real_RUL = prepareData()
    print(train_X[0:5])
    print(train_y[0:5])
    print(test_X[0:5])
    print(real_RUL[0:5]) 

    print(type(train_X))
    print(type(train_y))
    print(type(test_X))
















