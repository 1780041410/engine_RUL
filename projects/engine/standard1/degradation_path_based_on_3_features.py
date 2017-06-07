#!/usr/bin/env python
# coding=utf-8
'''
    说明：基于三个新的特征,可视化每个unit的 feature degradation path
          默认是随着cycle的变化，三维空间中的点
          [feature_in,feature_de,feature_mix]
          的变化轨迹
    结果：100条三维空间中的线-training set of data set 1
'''

import pandas as pd  
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 

#****************读入3个特征数据*****************#
index = ['unit','cycle','feature_in','feature_de','feature_mix']
index_f = ['feature_in','feature_de','feature_mix'] 
feature_3 = pd.read_table('new_features_3_train.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')

#********************提取数据********************#
last_row_num = len(feature_3) - 1
last_unit = int(feature_3.loc[last_row_num,'unit'])

three_dimension_list = []

for unit in range(1,last_unit+1):
    temp1 = feature_3[feature_3.unit==unit]
    temp2 = temp1.loc[:,index_f] 
    three_dimension_list.append(temp2)

#print(three_dimension_list[0:2])

#*****************用三维的散点图显示*******************#
fig = plt.figure()
#ax = plt.subplot(111,projection='3d')
ax = Axes3D(fig)  
for unit in range(len(three_dimension_list)):
    temp = three_dimension_list[unit]
    ax.scatter(temp.feature_mix,temp.feature_in,temp.feature_de)

ax.set_xlabel('feature_mix')
ax.set_ylabel('feature_in')
ax.set_zlabel('feature_de')
plt.show()






    







