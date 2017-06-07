#!/usr/bin/env python
# coding=utf-8
'''
    说明：将三个新特征对应的testing set中,
          每个unit最后一个cycle对应的特征向量
          提取出来，单独写入一个文件

    函数：filter函数非常好用，可以按照行列索引
          所满足的要求提取整个DataFrame中的数据
    
    注：这里没有使用filter函数

    提取思路：0---先按照unit进行行向分片;
              1---再在子片数据中按照cycle满足的条件提取对应的那一行
              2---cycle满足的条件由now_age_FD001的内容从上向下遍历控制
              3---用列表将每次提取的中间成果存起来
              4---使用 pd 的concat函数行向合并,即默认axis=0
              5---写出文件 
'''

import pandas as pd

# 读入数据
index  = ['unit','cycle','feature_in','feature_de','feature_mix']
index2 = ['cycle']
new_features_3_test = pd.read_table('new_features_3_test.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
now_age_FD001 = pd.read_table('now_age_FD001.txt',delim_whitespace=True,header=None,names=index2,encoding='utf-8')

# 提取每个unit对应的最后一个cycle的特征数据

test_X_temp = [] 
for unit in range(1,len(now_age_FD001)+1):
    now_age = now_age_FD001.cycle[unit-1]  #此处即使DataFrame只有一列数据,也不能直接像列表那样进行索引,必须先按照names提取出第一列,然后索引
    temp1 = new_features_3_test[new_features_3_test.unit==unit]
    temp2 = temp1[temp1.cycle==now_age] 
    test_X_temp.append(temp2)

test_X = pd.concat(test_X_temp)
test_X.to_csv('test_100_X_3_features_FD001.txt',index=False,header=False,sep=' ')















