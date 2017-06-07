#!/usr/bin/env python
# coding=utf-8
'''
    说明: 本文件的目的是将测试集合按照每个unit的第一个cycle数据，与训练集合的两个子集分别进行
          余弦相似度计算，然后将每个unit的数据归为与它最相似的训练集类做为对应的测试集合。

'''

import pandas as pd  
import numpy as np

def similarity(array1,array2):
    num = float(sum(array1*array2))
    denom = np.linalg.norm(array1)*np.linalg.norm(array2)
    cos = num/denom
    sim = 0.5 + 0.5*cos
    
    return sim       

def split_testing_set():
    index1 = ['unit','cycle','s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']
    index2 = ['s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']   
    early_failed_train = pd.read_table('early_failed_training_set.txt',delim_whitespace=True,header=None,names=index1,encoding='utf-8')
    later_failed_train = pd.read_table('later_failed_training_set.txt',delim_whitespace=True,header=None,names=index1,encoding='utf-8')
    test_14f = pd.read_table('after_mean_std_test_X.txt',delim_whitespace=True,header=None,names=index1,encoding='utf-8')

    early_train_unit_ID = set(early_failed_train.unit) 
    later_train_unit_ID = set(later_failed_train.unit)  
    

    unit_num = int(max(test_14f.unit))
    
    early_test = []
    later_test = []  
    for unit in range(1,unit_num+1):
        similarity_early = []
        similarity_later = []  
        
        temp1 = test_14f[test_14f.unit==unit]   
        temp1_test = temp1.loc[:,index2]    
        first_line_test  = temp1_test.head(1)
        first_array_test = first_line_test.values[0]
        
        for item in early_train_unit_ID:
            temp_early = early_failed_train.loc[early_failed_train.unit==item,index2]
            first_line_early  = temp_early.head(1) 
            first_array_early = first_line_early.values[0]

            similarity_early.append(similarity(first_array_test,first_array_early))  

        for item in later_train_unit_ID:
            temp_later = later_failed_train.loc[later_failed_train.unit==item,index2]
            first_line_later  = temp_later.head(1) 
            first_array_later = first_line_later.values[0]
            
            similarity_later.append(similarity(first_array_test,first_array_later))
         
        sim_early = np.mean(similarity_early)
        sim_later = np.mean(similarity_later) 

        if sim_early >= sim_later:
            early_test.append(temp1)
        else:
            later_test.append(temp1)   
        
    early_failed_test = pd.concat(early_test)
    later_failed_test = pd.concat(later_test)
    
    early_failed_test.to_csv('early_failed_test.txt',header=False,index=False,sep=' ')
    later_failed_test.to_csv('later_failed_test.txt',header=False,index=False,sep=' ') 



if __name__ == '__main__':
    split_testing_set()    






