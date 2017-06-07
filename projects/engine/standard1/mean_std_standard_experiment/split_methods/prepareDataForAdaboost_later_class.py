#!/usr/bin/env python
# coding=utf-8
'''
    说明： 载入数据,传给Adaboost regression 
    特征： early---14个sensor数据的标准化数据.

    | train_X |  
    | train_y |    
    | test_X  |        

'''
import pandas as pd 
import numpy as np 

def prepareData():

    index_14f_with_ID    = ['unit','cycle','s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']
    index_14f_without_ID = ['s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']
    index_y = ['unit','cycle','rul']
    index_unit_cycle_ID = ['unit','cycle']  
    index_c = ['real_rul']    
    
    real_RUL = pd.read_table('later_RUL_data.txt',delim_whitespace=True,header=None,names=index_c,encoding='utf-8')    

    train_X_temp  = pd.read_table('later_failed_training_set.txt',delim_whitespace=True,header=None,names=index_14f_with_ID,encoding='utf-8')

    test_X_temp   = pd.read_table('later_failed_testing_set.txt',delim_whitespace=True,header=None,names=index_14f_with_ID,encoding='utf-8')

    train_y_temp  = pd.read_table('later_train_y.txt',delim_whitespace=True,header=None,names=index_y,encoding='utf-8')

    #test_y_temp = pd.read_table('test_y_FD001.txt',delim_whitespace=True,header=None,names=index_c,encoding='utf-8')
    #real_RUL_temp = pd.read_table('RUL_FD001.txt',delim_whitespace=True,header=None,names=index_c,encoding='utf-8') 
    
    # 提取test_X的unit和cycle的编号,后文在将cycle层面的预测结果准换为unit层面的预测结果时使用 
    unit_cycle_ID_test = test_X_temp.loc[:,index_unit_cycle_ID]          
    
    # 训练数据
    train_X  = train_X_temp.loc[:,index_14f_without_ID]  
    train_X  = train_X.as_matrix()  # train_X

    train_y  = train_y_temp.rul.tolist()
    train_y  = np.array(train_y)    # train_y  
    
    #test_y = test_y_temp.rul.tolist()
    #test_y = np.array(test_y)    # test_y  
    
    # 预测数据 
    test_X   = test_X_temp.loc[:,index_14f_without_ID]
    test_X   = test_X.as_matrix()   # test_X  
    
    #real_RUL = real_RUL_temp.rul.tolist()
    #real_RUL = np.array(real_RUL)   # real_RUL  
    
    return train_X, train_y, test_X, unit_cycle_ID_test, real_RUL    




# 函数测试

if __name__ == '__main__':
    
    train_X,train_y,test_X,unit_cycle_ID_test,real_RUL = prepareData()
    
    print(real_RUL)  
    print(unit_cycle_ID_test)
    print(train_X[0:5])
    print(train_y[0:5])
    print(test_X[0:5])
    #print(test_X[0:5])
    #print(test_y[0:5])  

    #print(type(train_X))
    #print(type(train_y))
    #print(type(test_X))

    print(len(train_X))
    print(len(train_y))
    print(len(test_X))
    #print(len(real_RUL))   
    #print(len(test_y))  











