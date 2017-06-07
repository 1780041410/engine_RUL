#!/usr/bin/env python
# coding=utf-8

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats   

def get_life_and_firstVector_module():  
    index1 = ['unit','cycle','s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']
    index2 = ['s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']   
    train_14X = pd.read_table('after_mean_std_train_X.txt',delim_whitespace=True,header=None,names=index1,encoding='utf-8')
    
    unit_num = int(max(train_14X.unit))

    life_train = []
    firstVectorModule = []  

    for unit in range(1,unit_num+1):         
        temp1 = train_14X[train_14X.unit==unit]
        life_train.append(int(max(temp1.cycle)))
        temp2 = temp1.loc[:,index2]
        #first_vector = temp2.head(1)
        first_vector = temp2.tail(1)    
        first_vector = first_vector.values[0]
        first_vector_module = np.linalg.norm(first_vector)
        firstVectorModule.append(first_vector_module)      
    
    print(life_train)   
    #****************将life_train的数据标准化到module数据的最大值和最小值之间**************#
    max_module = np.max(firstVectorModule)
    min_module = np.min(firstVectorModule)
    max_life   = np.max(life_train)
    min_life   = np.min(life_train)   

    k = (max_module-min_module)/float(max_life-min_life)  
    
    life_train_s = [min_module+k*(item-min_life) for item in life_train]   
    

    return life_train_s, firstVectorModule  


if __name__ == '__main__':
    life, module = get_life_and_firstVector_module()    
    print('-----------------基本信息--------------------------')
    print(len(life))
    print(len(module))
    #print(life)
    #print(module)   
    print('-----------------相关系数--------------------------')
    #cor1 = stats.pearsonr(life,module)    
    cor2 = np.corrcoef(life,module)     
    #print(cor1)
    print(cor2)   
    
    X = range(100)
    plt.plot(X,life,'r-o') 
    plt.plot(X,module,'b-d')   
    plt.show()   


    #plt.hist(life_train,bins=35,alpha=.5)     



