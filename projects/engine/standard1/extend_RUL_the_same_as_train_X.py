#!/usr/bin/env python
# coding=utf-8
'''
    说明：本文件的目的是将训练数据的标签,按照与X相同的扩展方式
          进行对应扩展.
    结果：将promote之后的训练数据写出到文件中

'''

import pandas as pd

#**************************************************************读入数据************************************************************#
index = ['unit','cycle','feature_in','feature_de','feature_mix']
index2 = ['RUL']
index3 = ['unit','cycle']  
new_features_3_train = pd.read_table('new_features_3_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
train_y_FD001 = pd.read_table('train_y_FD001.txt',delim_whitespace=True,header=None,names=index2,encoding='utf-8')   
unit_cycle = new_features_3_train.loc[:,index3]

train_y = pd.concat([unit_cycle,train_y_FD001],axis=1)
train_y_copy = train_y.copy()   # 直接复制一份原数据,在操作的过程中,向这个副本中插入新增数据,并且使用浅拷贝模式,避免
                                # 在向副本中插入数据时原数据也被同样修改.


#***********************************************************定义计算y的函数********************************************************#
def compute_y(x,k):
    if x>k:
        return int(x-k)
    else:
        print("the cycle number is less than k !")


#***********************************************************进行promote操作********************************************************#

last_row  = len(train_y) - 1       #获取最后一行的行号(编号从0开始)
last_unit = int(train_y.loc[last_row,'unit'])  # 获取最后一个unit的编号    
final_result = []
for unit in range(1,last_unit+1):
    slice_by_unit = train_y[train_y.unit==unit] # 切片取出当前unit的所有数据
    result_temp = train_y_copy[train_y_copy.unit==unit]                   # 切片取出备份数据中当前unit的数据,等待插入
    k = int(slice_by_unit.cycle.quantile(0.75,interpolation='higher'))    # 提取当前unit的cycle的3/4分位数
    spin = k            # 用一个位置变量作为备份数据拆分边界的指针 
    promote_temp = slice_by_unit[slice_by_unit.cycle>k]                   # 提取3/4分位数之后的所有数据 
    for line in range(len(promote_temp)):
        promote_cycle = promote_temp.iloc[[line]]   
        cycle_temp = int(promote_cycle.cycle)    
        y = compute_y(cycle_temp,k)       
        inset_temp = [promote_cycle]*y
        inset_temp = pd.concat(inset_temp,axis=0)      
        above = result_temp.loc[:spin]    
        below = result_temp.loc[spin+1:] 
        result_temp = pd.concat([above,inset_temp,below],ignore_index=True)
        spin = spin + y + 1   
    final_result.append(result_temp)
    #print(final_result)   

final_result = pd.concat(final_result)   


#**************************************************************写出到文件********************************************************#
final_result.to_csv('extended_RUL_with_unit_cycle_ID_FD001.txt',index=False,header=False,sep=' ')




