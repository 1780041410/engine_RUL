#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import numpy as np   
def cycle_to_unit(y_pre,ID_test):
    index_age = ['age']      
    early_now_age = pd.read_table('later_now_age_data.txt',delim_whitespace=True,header=None,names=index_age,encoding='utf-8')
    y_pre = pd.DataFrame(y_pre)  
    y_pre = y_pre.rename(columns={0:'rul_pre'})   
    
    total_life = y_pre.rul_pre + ID_test.cycle
    
    total_life_with_ID = pd.concat([ID_test.unit,total_life],axis=1)
    total_life_with_ID = total_life_with_ID.rename(columns={0:'life_pre'})  

    set_unit_ID = set(total_life_with_ID.unit)  
    
    unit_life = []  
    for item in set_unit_ID:
        temp1 = total_life_with_ID[total_life_with_ID.unit==item] 
        avg_life = np.average(temp1.life_pre)
        unit_life.append(avg_life)
    
    unit_life = pd.DataFrame(unit_life)   
    unit_RUL = unit_life[0] - early_now_age.age 
    list_ID = list(set_unit_ID)   
    unit_ID = pd.DataFrame(list_ID)
    unit_ID = unit_ID.rename(columns={0:'unit'})  

    unit_RUL_with_ID = pd.concat([unit_ID,unit_RUL],axis=1)
    unit_RUL_with_ID = unit_RUL_with_ID.rename(columns={0:'RUL_pre'})         


    return  unit_RUL_with_ID                  

if __name__ == '__main__':
    unit_RUL_with_ID = cycle_to_unit()  
