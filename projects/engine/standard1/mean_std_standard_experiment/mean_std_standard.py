#!/usr/bin/env python
# coding=utf-8
'''
    说明: 本文件的目的是将数据进行 mean_std 标准化;
    步骤: 1. 读入原始数据 train 和 test;
          2. 提取出有预测力的指标;
          3. 对数据进行均值-方差标准化;
          4. 将结果写出到文件.
'''

import pandas as pd  
import numpy as np  

# 宏定义操作文件时的命名指标       
global index_all, index_14f_with_ID, index_14f_without_ID, index_ID

index_all = ['unit','cycle','op1','op2','op3','s1','s2','s3','s4','s5','s6','s7','s8',
             's9','s10','s11','s12','s13','s14','s15','s16','s17','s18','s19','s20','s21']

index_14f_with_ID    = ['unit','cycle','s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']
index_14f_without_ID = ['s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']

index_ID = ['unit','cycle']  

def mean_std_propre(dataframe):   
    
    max_unit = int(max(dataframe.unit))
    
    m_s_s_data = []   
    for unit in range(1,max_unit+1):
        temp1 = dataframe[dataframe.unit==unit] 
        temp2 = temp1.loc[:,index_14f_without_ID]
        temp3 = temp2.apply(lambda x:(x-np.mean(x))/np.std(x))
        m_s_s_data.append(temp3)

    return m_s_s_data    


def standardize_data_mean_std():
    
    # 读入原始数据  
    train = pd.read_table('train_FD001.txt',delim_whitespace=True,header=None,names=index_all,encoding='utf-8')
    test  = pd.read_table('test_FD001.txt',delim_whitespace=True,header=None,names=index_all,encoding='utf-8')

    # 提取出unit和cycle的ID号  
    unit_cycle_ID_train = train.loc[:,index_ID]
    unit_cycle_ID_test  = test.loc[:,index_ID]  
    
    # 提取出14个方差不为零的特征   
    need_propre_train = train.loc[:,index_14f_with_ID]     
    need_propre_test  = test.loc[:,index_14f_with_ID]  
    
    # 调用均值-方差函数进行标准化
    after_propre_list_train = mean_std_propre(need_propre_train)
    after_propre_list_test  = mean_std_propre(need_propre_test)  
    
    # 将上一步函数返回的DataFrame的列表合并成一个DataFrame  
    after_propre_dataframe_train = pd.concat(after_propre_list_train)
    after_propre_dataframe_test  = pd.concat(after_propre_list_test)   
    
    # 给标准化后的14列特征数据加上两列ID号  
    after_propre_train = pd.concat([unit_cycle_ID_train,after_propre_dataframe_train],axis=1)
    after_propre_test  = pd.concat([unit_cycle_ID_test,after_propre_dataframe_test],axis=1)  
    
    # 将结果写出到本地文件   
    after_propre_train.to_csv('after_mean_std_train_X.txt',header=False,index=False,sep=' ')
    after_propre_test.to_csv('after_mean_std_test_X.txt',header=False,index=False,sep=' ')


if __name__ == '__main__':
    standardize_data_mean_std()
    print('ok')







