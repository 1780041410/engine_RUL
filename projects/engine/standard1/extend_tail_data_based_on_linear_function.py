#!/usr/bin/env python
# coding=utf-8
'''
    说明：本文件的目的是将训练数据中的tail数据按照如下
          线性函数进行promote,使得tail部分的数据量增多
          为训练提供更多的degradation信息.
                     y = x - k
    解释：公式中的x代表某个unit的某一cycle,k代表当前unit
          的cycle的 3/4 分位点,y代表promote之后,在当前的
          unit中,该cycle共对应y+1条数据,我们首先求出y,然
          后将数据拷贝至y+1条.被promote的数据是3/4分位数
          之后的数据  
    结果：将promote之后的训练数据写出到文件中

'''

import pandas as pd

#**************************************************************读入数据************************************************************#
index = ['unit','cycle','feature_in','feature_de','feature_mix']
new_features_3_train = pd.read_table('new_features_3_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
result_train = new_features_3_train.copy()  # 直接复制一份原数据,在操作的过程中,向这个副本中插入新增数据,并且使用浅拷贝模式,避免
                                            # 在向副本中插入数据时原数据也被同样修改.


#***********************************************************定义计算y的函数********************************************************#
def compute_y(x,k):
    if x>k:
        return int(x-k)
    else:
        print("the cycle number is less than k !")


#***********************************************************进行promote操作********************************************************#

last_row  = len(new_features_3_train) - 1       #获取最后一行的行号(编号从0开始)
last_unit = int(new_features_3_train.loc[last_row,'unit'])  # 获取最后一个unit的编号    
final_result = []
for unit in range(1,last_unit+1):
    slice_by_unit = new_features_3_train[new_features_3_train.unit==unit] # 切片取出当前unit的所有数据
    result_temp = result_train[result_train.unit==unit]                   # 切片取出备份数据中当前unit的数据,等待插入
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
final_result.to_csv('extended_tail_data_train_X_FD001.txt',index=False,header=False,sep=' ')




