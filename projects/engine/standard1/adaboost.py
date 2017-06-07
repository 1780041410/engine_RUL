#!/usr/bin/env python
# coding=utf-8
'''
    版本： naive 
    说明： 采用 Adaboost regression 预测RUL
    特征： feature_in,feature_de,feature_mix
    train: 20631
    test : 100

'''
import prepareDataForAdaboost_2_features as pdfa    
import plotSorted as ps   
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree     import DecisionTreeRegressor
from sklearn.ensemble.forest import RandomForestRegressor  
#from sklearn import svm 
#from sklearn.neural_network import MLPRegressor  
#from sklearn import linear_model   
import numpy as np 
import math  

#*************************************************************训练和预测*********************************************************#
def AdaBoostRegression(train_X,train_y,test_X):      

    #*********#
    '''
    rng = np.random.RandomState(1)   
    regressor = AdaBoostRegressor(DecisionTreeRegressor(min_samples_leaf=5,max_depth=depth),
                                  n_estimators=num,learning_rate=0.9,loss='exponential',random_state=rng)
    regressor.fit(train_X,train_y)
    y_predict = regressor.predict(test_X)             
    #yy_predict = regressor.staged_predict(test_X)
    #path = regressor.decision_path(test_X)        # 回归树有这个方法,但是adaboost没有这个方法     
    #*********#
    '''
    
    '''
    reg = svm.SVR(kernel='rbf')
    reg.fit(train_X,train_y)  
    y_predict = reg.predict(test_X)      
    #*********#
    '''

    '''
    reg = RandomForestRegressor(n_estimators=200,max_depth=25)
    reg.fit(train_X,train_y)
    y_predict = reg.predict(test_X)   
    '''
    
    
    '''
    reg = linear_model.LogisticRegression(solver='sag')
    reg.fit(train_X,train_y)
    y_predict = reg.predict(train_X)  
    '''
    '''
    reg = MLPRegressor(hidden_layer_sizes=(100,100,50,50),activation='relu')  
    reg.fit(train_X,train_y)
    y_predict = reg.predict(train_X)  
    '''

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
    train_X,train_y,test_X,real_RUL = pdfa.prepareData()
    print(len(train_X))
    print(len(train_y))
    print(len(test_X))
    print(len(real_RUL))

    y_pre = AdaBoostRegression(train_X,train_y,test_X)         
    print(y_pre)   
    #S,M = score(real_RUL,y_pre)
    #print(S,M)   
    #e_MSE,e_MAE,e_MAPE,e_MSPE,e_pr = compute_5_error(real_RUL,y_pre)     
    #print("five kinds errors are following:")
    #print(e_MSE,e_MAE,e_MAPE,e_MSPE,e_pr)


    #score_record = {}      
    #num_depth_list = []
    #depth_list = []
    #score_list = []   
    #for num in range(100,200,5): 
    #    for depth in range(5,12):
    #        y_pre = AdaBoostRegression(train_X,train_y,test_X,depth,num)   
    #        S,M = score(real_RUL,y_pre)
    #        num_depth_list.append((num,depth))  
    #        score_list.append((S,M))   
    #        #score_record['num:depth'] = (S,M)   
    #        #print("the prediction result is following: ")
    #        #print(y_pre)        
    #print(num_depth_list)
    #print(score_list)

    #np.savetxt("Adaboost_pre_100_test_rul.txt",y_pre) # 用numpy的savetxt函数将预测结果写出到文件   
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

    ps.plotSorted(real_RUL,y_pre)         















