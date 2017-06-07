#!/usr/bin/env python
# coding=utf-8
'''
    说明：该文件对训练数据进行数据分布
          重置
    方法：将训练数据中,每个unit对应的cycle中，
          小于测试数据中最小当前cycle的数据先
          提出,将剩下的写出到文件，作为新的
          数据

'''
import pandas as pd 

#*****************读入数据******************#
index  = ['unit','cycle','feature_in','feature_de','feature_mix']
index2 = ['RUL']
index3 = ['unit','cycle'] 
new_features_3_train = pd.read_table('new_features_3_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
train_y_FD001        = pd.read_table('train_y_FD001.txt',delim_whitespace=True,header=None,names=index2,encoding='utf-8')   
unit_cycle = new_features_3_train.loc[:,index3]

#************** Reset train_X **************# 
reset_train_X_3f_bigger_31 = new_features_3_train[new_features_3_train.cycle>30.0]


#************** Reset train_y *************#
#unit_cycle = new_features_3_train.loc[:,index3]
have_unit_cycle_ID_train_y = [unit_cycle,train_y_FD001]
have_unit_cycle_ID_train_y = pd.concat(have_unit_cycle_ID_train_y,axis=1) # 纵向合并,axis=1
reset_train_y_bigger_31    = have_unit_cycle_ID_train_y[have_unit_cycle_ID_train_y.cycle>30.0]
reset_train_y_bigger_31    = reset_train_y_bigger_31.RUL   # 为了调用以前写的用来读入训练数据的代码，这里直接提取 train_y 的RUL  

#******************写出数据****************#
reset_train_X_3f_bigger_31.to_csv('reset_train_X_3f_bigger_31.txt',index=False,header=False,sep=' ')
reset_train_y_bigger_31.to_csv('reset_train_y_bigger_31.txt',index=False,header=False,sep=' ')












