#!/usr/bin/env python
# coding=utf-8
'''
    说明: 本文件的目的是给 test_y 的预测结果加上unit和cycle的
          ID号,并且将cycle层面的预测结果转换为unit层面的预测,
          平均的方式暂时采用直接平均.    

''' 
import pandas as pd
import numpy as np   

def cycle_level_2_unit_level(cycle_level_prediction,diff_test_X):       
   
    cycle_based_pred_results = pd.DataFrame(cycle_level_prediction)   
    
    cycle_based_pred_results = cycle_based_pred_results.rename(columns={0:'rul'})       

    #index = ['unit','cycle','sensor2','sensor3','sensor4',
    #         'sensor7','sensor8','sensor9','sensor11','sensor12',
    #         'sensor13','sensor14','sensor15','sensor17','sensor20','sensor21']

    index_unit_cycle = ['unit','cycle'] 
    index_unit = ['unit'] 
    index_rul = ['rul']
    index_age = ['age']   

    #diff_test_X = pd.read_table('diff_test_X.txt',delim_whitespace=True,header=None,names=index,encoding='utf-8')
    unit_cycle_ID = diff_test_X.loc[:,index_unit_cycle]   
    unit_ID = diff_test_X.loc[:,index_unit]   

    now_age_FD001 = pd.read_table('now_age_FD001.txt',delim_whitespace=True,header=None,names=index_age,encoding='utf-8')  
    cycle_based_pred_results_with_ID = pd.concat([unit_cycle_ID,cycle_based_pred_results],axis=1)

    total_cycles = cycle_based_pred_results_with_ID.cycle + cycle_based_pred_results_with_ID.rul       

    total_cycles_with_ID = pd.concat([cycle_based_pred_results_with_ID.unit,total_cycles],axis=1)

    last_unit = int(max(total_cycles_with_ID.unit))

    final_results = []

    for unit in range(1,last_unit+1):
        temp1 = total_cycles_with_ID[total_cycles_with_ID.unit==unit] 
        final_results.append(np.average(temp1[0]))

    #print(final_results[0:10])
    #INPUT = input()   
    final_results_dataFrame = pd.DataFrame(final_results)
    final_results_dataFrame = final_results_dataFrame.T   
    
    prediction_for_100_unit = final_results_dataFrame - now_age_FD001.age
    #prediction_for_100_unit.to_csv('prediction_for_unit_RUL.txt',header=False,index=False,sep=' ')   
    
    return prediction_for_100_unit    

if __name__ == '__main__':
    p = pd.DataFrame([5]*12996)
    d = cycle_level_2_unit_level(p)
    print(d)  








