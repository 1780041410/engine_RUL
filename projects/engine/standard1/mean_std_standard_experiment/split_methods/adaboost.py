#!/usr/bin/env python
# coding=utf-8
'''
    版本： version mean_std data 2.0   
    说明： 采用 Adaboost regression 预测   

'''
import cycle_to_unit_early as ctu_early    
import cycle_to_unit_later as ctu_later        
import prepareDataForAdaboost_early_class as pdfa_early 
import prepareDataForAdaboost_later_class as pdfa_later    
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree     import DecisionTreeRegressor
import numpy as np 
import math 
import pandas as pd  
import matplotlib.pyplot as plt   
import plotSorted_early as pls_e  
import plotSorted_later as pls_l    

#*************************************************************训练和预测*********************************************************#
def AdaBoostRegression(train_X,train_y,test_X,depth,num):        
    rng = np.random.RandomState(1)   
    regressor = AdaBoostRegressor(DecisionTreeRegressor(max_depth=depth),n_estimators=num,learning_rate=0.9,loss='exponential',random_state=rng)
    regressor.fit(train_X,train_y) 
    y_predict = regressor.predict(test_X)                        

    return y_predict        


#*************************************************************计算五种误差*********************************************************#
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

#**************************************************************计算M_score********************************************************#
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


#***********************************************************可视化对比并保存图片**************************************************#
def plot_figure(real_RUL,unit_level_pre,num,depth):

    x = range(100)  
    
    fig = plt.figure()   
    plt.plot(x,real_RUL,'r-o')
    plt.plot(x,unit_level_pre,'b-d')
    plt.savefig("m_s_results/Adaboost_expLoss_14f_%s_%s.png" %(num,depth))
    plt.clf()
    plt.close()   


def plot_figure_early(real_RUL_early,pre_RUL_early,depth,num):
    
    x = range(45)    
    
    fig = plt.figure()   
    plt.plot(x,real_RUL_early.real_rul,'r-o')
    plt.plot(x,pre_RUL_early.RUL_pre,'b-d')
    plt.savefig("search_num_depth_early/Split_adaboost_expLoss_14f_early_%s_%s.png" %(depth,num))   
    plt.clf()
    plt.close()   


def plot_figure_later(real_RUL_later,pre_RUL_later,depth,num):
 
    x = range(55)    
    
    fig = plt.figure()  
    plt.plot(x,real_RUL_later.real_rul,'r-o')
    plt.plot(x,pre_RUL_later.RUL_pre,'b-d')
    plt.savefig("search_num_depth_later/Split_adaboost_expLoss_14f_later_%s_%s.png" %(depth,num))     
    plt.clf()
    plt.close()   



#****************************************************************主函数测试*******************************************************#
if __name__ == '__main__':

    #*************************  分别载入 early 和 later 数据 ******************************#
    train_X_early, train_y_early, test_X_early, unit_cycle_ID_test_early, real_RUL_early = pdfa_early.prepareData()   
    train_X_later, train_y_later, test_X_later, unit_cycle_ID_test_later, real_RUL_later = pdfa_later.prepareData()       
    print("**************************数据导入成功*************************")
    
    for depth in range(20,21):       
        for num in range(800,805,5):   
            early_y_pre = AdaBoostRegression(train_X_early,train_y_early,test_X_early,depth,num) # 在cycle级别的预测     
            later_y_pre = AdaBoostRegression(train_X_later,train_y_later,test_X_later,depth,num)            
            pre_RUL_early = ctu_early.cycle_to_unit(early_y_pre,unit_cycle_ID_test_early)       # cycle级别的预测转换为unit级别
            pre_RUL_later = ctu_later.cycle_to_unit(later_y_pre,unit_cycle_ID_test_later)    
            plot_figure_early(real_RUL_early,pre_RUL_early,depth,num)
            plot_figure_later(real_RUL_later,pre_RUL_later,depth,num) 
            pls_e.plotSorted(real_RUL_early.real_rul,pre_RUL_early.RUL_pre,depth,num)
            pls_l.plotSorted(real_RUL_later.real_rul,pre_RUL_later.RUL_pre,depth,num)
            print("****************参数_depth=%s_and_num=%s训练成功*****************" %(depth,num))   















