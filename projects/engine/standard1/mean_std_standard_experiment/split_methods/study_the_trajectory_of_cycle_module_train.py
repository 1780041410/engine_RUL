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

    VectorModule = []  

    for unit in range(1,unit_num+1):
        temp1 = train_14X[train_14X.unit==unit]
        temp2 = temp1.loc[:,index2]
        temp3 = temp2.as_matrix()   
        module = [np.linalg.norm(item) for item in temp3]
        VectorModule.append(module)   

    return VectorModule      


if __name__ == '__main__':
    module = get_life_and_firstVector_module()    
    #print('-----------------基本信息--------------------------')
    #print(len(module))
    #print(module[0])   
    #print(len(module[0]))
    #print(len(module[1]))    
    
    #X = range(100)
    #plt.plot(X,life,'r-o') 
    #plt.plot(X,module,'b-d')   
    #for item_list in module:
    #plt.plot(module[0])   
    #plt.plot(module[50])
    plt.plot(module[99])   
    plt.show()   

    #plt.hist(life_train,bins=35,alpha=.5)     



