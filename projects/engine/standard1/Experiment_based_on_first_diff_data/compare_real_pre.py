#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import math    
import numpy as np   
#import plotSorted as ps
import matplotlib.pyplot as plt   



def score(true_rul,pre_rul):
    S1,S2 = 0,0
    d = [x-y for x,y in zip(pre_rul,true_rul)]
    n = len(d)   
    for i in range(n):
        if d[i] <= 0:
            S1 += math.exp(-d[i]/float(13))-1
        elif d[i] > 0:
            S2 += math.exp(d[i]/float(10))-1

    S = S1 + S2
    M_score = float(S)/n         

    return S, M_score     


def compute_5_error(true_rul,pre_rul):
    e_mse,e_mae,e_mape,e_mspe,e_pr,temp_a,temp_b = 0,0,0,0,0,0,0
    n = len(true_rul)
    m = len(pre_rul)
    true_rul_avg = np.mean(true_rul)
    pre_rul_avg = np.mean(pre_rul)
    
    if n==m:
        for i in range(n):
            e_mse += (true_rul[i] - pre_rul[i])**2
            e_mae += abs(true_rul[i] - pre_rul[i])
            e_mape += abs((true_rul[i] - pre_rul[i])/float(true_rul[i]))
            e_mspe += ((true_rul[i] - pre_rul[i])/float(true_rul[i]))**2
            e_pr += (true_rul[i] - true_rul_avg)*(pre_rul[i] - pre_rul_avg)

            temp_a += (true_rul[i] - true_rul_avg)**2
            temp_b += (pre_rul[i] - pre_rul_avg)**2

    else:
        print('the length of the true_rul and the pre_rul are not equal!')

    e_MSE = (math.sqrt(e_mse))/float(n)
    e_MAE = e_mae/float(n)
    e_MAPE = e_mape/float(n)
    e_MSPE = (math.sqrt(e_mspe)/float(n))
    e_pr = e_pr/float(math.sqrt(temp_a)*math.sqrt(temp_b))
    e_pr = 1 - e_pr 

    return e_MSE,e_MAE,e_MAPE,e_MSPE,e_pr 


if __name__ == '__main__':
    index = ['rul']
    RUL_FD001 = pd.read_table('RUL_FD001.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
    prediction_for_unit_rul = pd.read_table('prediction_for_unit_RUL.txt',delim_whitespace=True,header=None,names=None,encoding='utf-8')
    prediction_for_unit_rul = prediction_for_unit_rul.T    
    real_RUL = RUL_FD001.rul.tolist()
    prediction_for_unit_rul = prediction_for_unit_rul[0].tolist() 
    
    S,M = score(real_RUL,prediction_for_unit_rul)
    e1,e2,e3,e4,e5 = compute_5_error(real_RUL,prediction_for_unit_rul)   
    print(S,M)
    print(e1,e2,e3,e4,e5)
    x = range(100)   
    plt.plot(x,real_RUL,'r-o')
    plt.plot(x,prediction_for_unit_rul,'b-d')   
    plt.show()    





    #ps.plotSorted(real_RUL,prediction_for_unit_rul)    
    
    
    
    #print(real_RUL)
    #print(prediction_for_unit_rul)   
    
