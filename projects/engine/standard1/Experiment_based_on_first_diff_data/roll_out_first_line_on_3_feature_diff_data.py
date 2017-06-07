#!/usr/bin/env python
# coding=utf-8
'''
    说明:  本文件的目的是将差分数据中,每个unit的第一行删掉,因为
           第一行除了一个unit和cycle的编号外,没有数据.
    结果:  包括训练集合和测试集合.
    思路:  将原数据导入之后,首先按照unit的编号进行分割,然后在单个
           unit中,将cycle值在2及其以上的数据提取出来,最后将结果合并.  
'''

import pandas as pd 
import numpy as np 

def roll_out_first_row(dataframe):
    result = []  
    last_row = len(dataframe)-1
    print(last_row)    
    last_unit = int(dataframe.loc[last_row,'unit'])   
    for unit in range(1,last_unit+1):
        temp1 = dataframe[dataframe.unit==unit]
        temp2 = temp1[temp1.cycle>=2]
        result.append(temp2)
    
    final_out = pd.concat(result,axis=0)   
    
    return final_out    


def prepareData():

    #*************************************************************读入待处理数据**********************************************************#
    index   = ['unit','cycle','feature_in','feature_de','feature_mix'] 
    
    index_f = ['feature_in','feature_de','feature_mix'] 
    
    train_X_temp  = pd.read_table('diff_data_of_3_features_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
    test_X_temp   = pd.read_table('diff_data_of_3_features_test.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')

    #*************************************************调用函数处理数据并写出到文件*****************************************************#
    final_train_X = roll_out_first_row(train_X_temp)
    final_train_X.to_csv('diff_data_of_3_features_yes_train.txt',header=False,index=False,sep=' ')
    print('ok') 
    final_test_X  = roll_out_first_row(test_X_temp)
    final_test_X.to_csv('diff_data_of_3_features_yes_test.txt',header=False,index=False,sep=' ')
    print('ok')  
    
# 函数测试

if __name__ == '__main__':
    prepareData()
















