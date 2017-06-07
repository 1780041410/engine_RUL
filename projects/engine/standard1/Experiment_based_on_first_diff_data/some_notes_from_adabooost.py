#!/usr/bin/env python
# coding=utf-8

#from sklearn.ensemble.forest import RandomForestRegressor  
#from sklearn import svm 
#from sklearn.neural_network import MLPRegressor  
#from sklearn import linear_model   

#yy_predict = regressor.staged_predict(test_X)
#path = regressor.decision_path(test_X)        # 回归树有这个方法,但是adaboost没有这个方法     




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

