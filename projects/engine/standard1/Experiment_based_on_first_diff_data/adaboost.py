#!/usr/bin/env python
# coding=utf-8
'''
    版本： naive 
    说明： 采用 Adaboost regression 预测RUL
    特征： feature_in,feature_de,feature_mix
    train: 20631
    test : 100

'''
import plotSorted as pls   
import from_cycle_level_2_unit_level as fctou
import prepareDataForAdaboost_diff_14 as pdfa      
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree     import DecisionTreeRegressor
import numpy as np 
import math 
import matplotlib.pyplot as plt   

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



if __name__ == '__main__':
    train_X,train_y,test_X, real_RUL, diff_test_X = pdfa.prepareData()

    print(len(train_X))
    print(len(train_y))
    print(len(test_X))
    print(len(real_RUL))

    y_pre = AdaBoostRegression(train_X,train_y,test_X,7,200)   
    
    
    unit_level_pre = fctou.cycle_level_2_unit_level(y_pre,diff_test_X)     
    unit_level_pre = unit_level_pre.T
    unit_level_pre = unit_level_pre[0].tolist()
    S,M = score(real_RUL,unit_level_pre)  
    e1,e2,e3,e4,e5 = compute_5_error(real_RUL,unit_level_pre)
   
    print(unit_level_pre)
    print(S,M)
    print(e1,e2,e3,e4,e5)  
    
    x = range(100)  
    plt.plot(x,real_RUL,'r-o')
    plt.plot(x,unit_level_pre,'b-d')  
    plt.show()   
    
    pls.plotSorted(real_RUL,unit_level_pre)         
    
    
    #five_error_list = []
    #num_depth_list = []
    #score_list = []
    #depth = 7
    #num = 150






'''
    for num in range(50,100,5): 
        for depth in range(8,16):   
            num_depth_list.append((num,depth))  
            y_pre = AdaBoostRegression(train_X,train_y,test_X,depth,num)   
            unit_level_pre = fctou.cycle_level_2_unit_level(y_pre,diff_test_X)     
            unit_level_pre = unit_level_pre.T
            unit_level_pre = unit_level_pre[0].tolist()
            S,M = score(real_RUL,unit_level_pre)  
            score_list.append((S,M))
            e1,e2,e3,e4,e5 = compute_5_error(real_RUL,unit_level_pre)
            five_error_list.append((e1,e2,e3,e4,e5))   
'''   

    
    
    #np.savetxt('RUL_prediction_7_150_3_new_f.txt',unit_level_pre)      
    #five_error_list.append([e1,e2,e3,e4,e5])
    #print(num_depth_list)
    #print(five_error_list)    
    #print(score_list)

    #for item in yy_predict:
    #    print(item)   

    #print(y_pre[0:200])
    #print(yy_predict[0:400])   
    
    #e_MSE,e_MAE,e_MAPE,e_MSPE,e_pr = compute_5_error(real_RUL,y_pre)     
    #print("five kinds errors are following:")
    #print(e_MSE,e_MAE,e_MAPE,e_MSPE,e_pr)

    #S,M_score = score(real_RUL,y_pre) 
    #print("the S_score and M_score are following : ")
    #print(S,M_score)  
















