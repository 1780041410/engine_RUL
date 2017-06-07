#!/usr/bin/env python
# coding=utf-8
'''
    说明：将真实的RUL按照从低到高的顺序
          排列并可视化,将预测结果的对比
          线条也可视化. 

'''

import matplotlib.pyplot as plt 
import numpy as np 

def plotSorted(real_RUL,pre_RUL,depth,num):  
    
    #***************************************获取排序后的index**********************************#
    m = len(real_RUL)
    pre_RUL  = pre_RUL.tolist()   
    real_RUL = real_RUL.tolist()
    real_RUL_p = real_RUL[:]    
    index_base = range(m)   
    tuple_temp = [(x,y) for x,y in zip(index_base,real_RUL)]
    dict_temp1 = dict(tuple_temp)
    dict_temp2 = sorted(dict_temp1.items(),key=lambda d:d[1],reverse=False)
    sorted_index = [item[0] for item in dict_temp2]
    
    #********************************************可视化****************************************#
    real_RUL_p.sort()
    #pre_RUL.sort()   

    pre_RUL_p = [pre_RUL[v] for v in sorted_index]
    
    fig = plt.figure()  
    plt.plot(real_RUL_p)
    plt.plot(pre_RUL_p)
    plt.savefig("search_num_depth_early/Sorted_Split_adaboost_14f_early_%s_%s.png" %(depth,num))  
    plt.clf()
    plt.close()        


if __name__ == '__main__':
    p = np.array([11,37,10,13,44,16])   
    q = np.array([12,34,12,11,45,18])  
    plotSorted(q,p)




