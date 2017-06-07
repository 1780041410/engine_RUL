#!/usr/bin/env python
# coding=utf-8
'''
    版本： version mean_std data 2.0   
    说明： 采用 Adaboost regression 预测RUL
    特征： 经过均值方差标准化后的14个特征对应的数据  
    train: 20631
    test : 100

'''
import from_cycle_level_2_unit_level as fctou
import prepareDataForAdaboost_m_s_14features as pdfa      
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree     import DecisionTreeRegressor
import numpy as np 
import math 
import matplotlib.pyplot as plt   
import plotSorted as pls   

#*************************************************************训练和预测*********************************************************#
def AdaBoostRegression(test_X,test_y,train_X,depth,num):        
    rng = np.random.RandomState(1)   
    regressor = AdaBoostRegressor(DecisionTreeRegressor(max_depth=depth),n_estimators=num,learning_rate=0.9,loss='exponential',random_state=rng)
    regressor.fit(test_X,test_y) 
    y_predict = regressor.predict(train_X)                    

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


#****************************************************************主函数测试*******************************************************#
if __name__ == '__main__':
    train_X, train_y, test_X, test_y = pdfa.prepareData()

    print(len(train_X))
    print(len(train_y))
    print(len(test_X))
    print(len(test_y))
    
    y_pre = AdaBoostRegression(test_X,test_y,train_X,7,200)        

    #unit_level_pre = fctou.cycle_level_2_unit_level(y_pre,unit_cycle_ID_train)        
    #unit_level_pre = unit_level_pre.T
    #unit_level_pre = unit_level_pre[0].tolist()
    S,M = score(train_y,y_pre)    
    print((M,S)) 
    e1,e2,e3,e4,e5 = compute_5_error(train_y,y_pre)  
    print((e1,e2,e3,e4,e5))  

    x = range(20631)    
    plt.plot(x,train_y,'r-o')
    plt.plot(x,y_pre,'b-d')  
    plt.show()   

    #pls.plotSorted(train_y,y_pre)   


    #five_error_list = []
    #num_depth_list = []
    #score_list = []
    #depth = 7
    #num = 150   

'''
    for num in range(150,250,3): 
        for depth in range(4,6):    
            num_depth_list.append((num,depth))  
            y_pre = AdaBoostRegression(train_X,train_y,test_X,depth,num)   
            unit_level_pre = fctou.cycle_level_2_unit_level(y_pre,unit_cycle_ID_test)        
            unit_level_pre = unit_level_pre.T
            unit_level_pre = unit_level_pre[0].tolist()
            S,M = score(real_RUL,unit_level_pre)  
            score_list.append((S,M))
            e1,e2,e3,e4,e5 = compute_5_error(real_RUL,unit_level_pre)
            five_error_list.append([e1,e2,e3,e4,e5])     
            plot_figure(real_RUL,unit_level_pre,num,depth)   
    
    #np.savetxt('RUL_prediction_7_150_3_new_f.txt',unit_level_pre)      
    #five_error_list.append([e1,e2,e3,e4,e5])
    print(num_depth_list)
    print(five_error_list)    
    print(score_list)

'''
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

    #ps.plotSorted(real_RUL,y_pre)         















