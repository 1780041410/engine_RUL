#!/usr/bin/env python
# coding=utf-8
'''
    说明： 载入数据,传给Adaboost regression 
    特征： 3个新feature的数据的一阶差分数据,每个unit的cycle计数从2开始.

'''
import pandas as pd 
import numpy as np 

def prepareData():


    index   = ['unit','cycle','feature_in','feature_de','feature_mix']  

    index_f = ['feature_in','feature_de','feature_mix']  

    index_c = ['unit','cycle','RUL']  

    index_r = ['RUL']  
    
    train_X_temp  = pd.read_table('diff_data_of_3_features_yes_train.txt',delim_whitespace=True,
                                          header=None,names=index,encoding='utf-8')

    test_X_temp   = pd.read_table('diff_data_of_3_features_yes_test.txt',delim_whitespace=True,
                                          header=None,names=index,encoding='utf-8')

    train_y_temp  = pd.read_table('diff_train_y.txt',delim_whitespace=True,header=None,names=index_c,encoding='utf-8')

    real_RUL_temp = pd.read_table('RUL_FD001.txt',delim_whitespace=True,header=None,names=index_r,encoding='utf-8') 
   
    # 训练数据
    train_X  = train_X_temp.loc[:,index_f] 
    train_X  = train_X.as_matrix()  # train_X

    train_y  = train_y_temp.RUL.tolist()    
    train_y  = np.array(train_y)    # train_y  
    
    # 预测数据 
    test_X   = test_X_temp.loc[:,index_f]
    test_X   = test_X.as_matrix()   # test_X  
    
    real_RUL = real_RUL_temp.RUL.tolist()     
    real_RUL = np.array(real_RUL)   # real_RUL  
    
    return train_X, train_y, test_X, real_RUL, test_X_temp               




# 函数测试

if __name__ == '__main__':
    train_X,train_y,test_X,real_RUL, diff_test_X = prepareData()
    print(train_X[0:5])
    print(train_y[0:5])
    print(test_X[0:5])
    print(real_RUL[0:5]) 

    print(type(train_X))
    print(type(train_y))
    print(type(test_X))






 









