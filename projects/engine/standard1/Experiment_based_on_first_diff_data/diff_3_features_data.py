#!/usr/bin/env python
# coding=utf-8
import pandas as pd 
import numpy as np 


'''
    说明: 本文件的目标是对feature_in, feature_de, feature_mix 三个新特征构成的数据集
          以unit为单位,进行一节差分.然后测试预测效果的好坏.

'''

def data_standardize():

    index  = ['unit','cycle','feature_in','feature_de','feature_mix']    
    index2 = ['feature_in','feature_de','feature_mix']   
    index3 = ['unit','cycle']   

    new_features_3_train = pd.read_table('new_features_3_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
    new_features_3_test  = pd.read_table('new_features_3_test.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
    
    max_unit_train = int(max(new_features_3_train.unit)) 
    max_unit_test  = int(max(new_features_3_test.unit))   
    
    sub_data_frame_train = []
    sub_data_frame_test  = []

    for unit in range(1,max_unit_train+1):
        temp1 = new_features_3_train[new_features_3_train.unit==unit]
        temp2 = temp1.loc[:,index2]
        sub_data_frame_train.append(temp2)

    for unit in range(1,max_unit_test+1):
        temp1 = new_features_3_test[new_features_3_test.unit==unit]
        temp2 = temp1.loc[:,index2]
        sub_data_frame_test.append(temp2)
    
    unit_cycle_id_train = new_features_3_train.loc[:,index3]
    unit_cycle_id_test  = new_features_3_test.loc[:,index3]  

    #*******************************************构造分片一阶差分数据*************************************************#
    # 列表解析进行一阶差分
    diff_3_feature_train_list = [dataframe.diff() for dataframe in sub_data_frame_train]
    diff_3_feature_test_list  = [dataframe.diff() for dataframe in sub_data_frame_test]    

    #*******************************************将分片一阶差分数据写出到文件*******************************************#
    tmp_first_diff_based_on_standard_train = pd.concat(diff_3_feature_train_list)
    temp_list3 = [unit_cycle_id_train,tmp_first_diff_based_on_standard_train]
    final_first_diff_based_on_standard_train = pd.concat(temp_list3,axis=1) 
    final_first_diff_based_on_standard_train.to_csv('diff_data_of_3_features_train.txt',index=False,header=False,sep=' ')
    
    tmp_first_diff_based_on_standard_test  = pd.concat(diff_3_feature_test_list)
    temp_list3 = [unit_cycle_id_test,tmp_first_diff_based_on_standard_test]  
    final_first_diff_based_on_standard_test = pd.concat(temp_list3,axis=1) 
    final_first_diff_based_on_standard_test.to_csv('diff_data_of_3_features_test.txt',index=False,header=False,sep=' ')

    return final_first_diff_based_on_standard_train,final_first_diff_based_on_standard_test

    

if __name__ == '__main__':
    df1,df2 = data_standardize()
    #print(len(list2))
    #print(type(list2))
    #print(list1[1])
    #print(len(list1))

    #print(diff1[1])
    print(len(df1))
    print(df1) 









