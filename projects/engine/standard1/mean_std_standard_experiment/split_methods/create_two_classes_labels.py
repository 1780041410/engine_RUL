#!/usr/bin/env python
# coding=utf-8
'''
    说明: 本文件的目的是为分割后的训练数据构造对应的label,
          将原有的label进行对应的分割
        
          early_train_X ---> early_train_y
          early_test_X  ---> early_test_y  

          later_train_X ---> later_train_y 
          later_test_X  ---> later_test_y  

'''
import pandas as pd
import numpy as np

def create_label():
    index1 = ['unit']
    index2 = ['unit','cycle','rul']

    early_train_X_unit_ID = pd.read_table('early_failed_training_set.txt',delim_whitespace=True,usecols=[0],names=index1,encoding='utf-8')
    early_unit_ID = set(early_train_X_unit_ID.unit)
    
    later_train_X_unit_ID = pd.read_table('later_failed_training_set.txt',delim_whitespace=True,usecols=[0],names=index1,encoding='utf-8') 
    later_unit_ID = set(later_train_X_unit_ID.unit)  

    train_y_total = pd.read_table('train_y_FD001_with_ID.txt',delim_whitespace=True,header=None,names=index2,encoding='utf-8')
    
    early_failed_label = []  
    for item in early_unit_ID:
        temp1 = train_y_total[train_y_total.unit==item]
        early_failed_label.append(temp1)
    
    later_failed_label = []   
    for item in later_unit_ID:
        temp1 = train_y_total[train_y_total.unit==item]
        later_failed_label.append(temp1) 
    
    early_train_y = pd.concat(early_failed_label)
    later_train_y = pd.concat(later_failed_label)

    early_train_y.to_csv('early_train_y.txt',header=False,index=False,sep=' ')
    later_train_y.to_csv('later_train_y.txt',header=False,index=False,sep=' ')

    #return early_train_y, later_train_y     





if __name__ == '__main__':
    create_label()
   
    #print(len(rr))   
    #print(len(pp))  












