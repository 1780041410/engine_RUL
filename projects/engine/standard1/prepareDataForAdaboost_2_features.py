#!/usr/bin/env python
# coding=utf-8
'''
    说明： 载入数据,传给Adaboost regression
           去掉混合特征 feature_mix.  
    特征： feature_in,feature_de     
    实验： 暂时不进行数据的promote操作  
    train_X  | 20631  
    train_y  | 20631     
    test_X   | 100   
    real_RUL | 100     

'''

import pandas as pd 
import numpy as np 

def prepareData():
    index   = ['unit','cycle','feature_in','feature_de','feature_mix']
    index_f = ['feature_in','feature_de']    # 和之前比,去掉了混合特征          
    index_c = ['rul']    
    
    train_X_temp  = pd.read_table('new_features_3_train.txt',delim_whitespace=True,
                                          header=None,names=index,encoding='utf-8')  # 这里暂时取没有promote过的数据   
    

    test_X_temp   = pd.read_table('test_100_X_3_features_FD001.txt',delim_whitespace=True,
                                          header=None,names=index,encoding='utf-8')

    train_y_temp  = pd.read_table('train_y_FD001.txt',delim_whitespace=True,header=None,names=index_c,encoding='utf-8')

    real_RUL_temp = pd.read_table('RUL_FD001.txt',delim_whitespace=True,header=None,names=index_c,encoding='utf-8') 
   
    # 训练数据
    train_X  = train_X_temp.loc[:,index_f] 
    train_X  = train_X.as_matrix()  # train_X

    train_y  = train_y_temp.rul.tolist()
    train_y  = np.array(train_y)    # train_y  
    
    # 预测数据 
    test_X   = test_X_temp.loc[:,index_f]
    test_X   = test_X.as_matrix()   # test_X  
    
    real_RUL = real_RUL_temp.rul.tolist()
    real_RUL = np.array(real_RUL)   # real_RUL  
    
    return train_X, train_y, test_X, real_RUL   




# 函数测试

if __name__ == '__main__':
    train_X,train_y,test_X,real_RUL = prepareData()
    print(len(train_X))
    print(len(train_y))
    print(len(test_X))
    print(len(real_RUL))  

    #print(type(train_X))
    #print(type(train_y))
    #print(type(test_X))
    #print(type(real_RUL))   















