#!/usr/bin/env python
# coding=utf-8
import pandas as pd 
import matplotlib.pyplot as plt 

index   = ['unit','cycle','feature_in','feature_de','feature_mix']
index_f = ['feature_in','feature_de']    # 和之前比,去掉了混合特征
train_X_temp  = pd.read_table('new_features_3_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')

last_row = len(train_X_temp) - 1
last_unit = int(train_X_temp.loc[last_row,'unit'])  

for unit in range(last_unit):
    temp1 = train_X_temp[train_X_temp.unit==unit]
    temp2 = temp1.feature_de
    plt.plot(temp2)

plt.show()


'''
train_feature_in = train_X_temp.loc[:,'feature_in']
train_feature_de = train_X_temp.loc[:,'feature_de']

plt.plot(train_feature_in)
plt.show()
'''




