#!/usr/bin/env python
# coding=utf-8
'''
    说明: 本文件的目的是将training集合按照寿命的大小，
          分为两个子训练集合，分割边界为寿命的均值
          
          第一类: early_failed
          第二类: later_failed

'''


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

def split_training_set_into_two_parts():
    index1 = ['unit','cycle','s2','s3','s4','s7','s8','s9','s11','s12','s13','s14','s15','s17','s20','s21']
    train_14X = pd.read_table('after_mean_std_train_X.txt',delim_whitespace=True,header=None,names=index1,encoding='utf-8')
    
    unit_num = int(max(train_14X.unit))

    life_train = [] 
    for unit in range(1,unit_num+1):
        temp1 = train_14X[train_14X.unit==unit]
        life_train.append(int(max(temp1.cycle)))

    split_mean = np.mean(life_train)   

    early_failed = []
    later_failed = []  
    for unit in range(1,unit_num+1):
        temp2 = train_14X[train_14X.unit==unit]
        unit_life = int(max(temp2.cycle))
        if unit_life >= split_mean:
            later_failed.append(temp2)
        else:
            early_failed.append(temp2)
    
    early_failed_dataframe = pd.concat(early_failed,ignore_index=True)   
    later_failed_dataframe = pd.concat(later_failed,ignore_index=True)
    
    early_failed_dataframe.to_csv('early_failed_training_set.txt',header=False,index=False,sep=' ')
    later_failed_dataframe.to_csv('later_failed_training_set.txt',header=False,index=False,sep=' ') 

    return early_failed_dataframe, later_failed_dataframe



if __name__ == '__main__':
    
    pd1, pd2 = split_training_set_into_two_parts()
 
 
    #print("早fail的发动机为：")
    #print(pd1)
    #print("晚fail的发动机为：")
    #print(pd2)  

    #print(len(pd1)) 
    #print(len(pd2))  


    #print("训练集合寿命的三个统计量：")
    
    #print(np.mean(list1))
    #print(np.min(list1))
    #print(np.max(list1))
    
    #print("训练集合的寿命向量为：")
    #print(list1)   
    #plt.plot(list1)   
    #plt.show()








