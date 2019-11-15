import numpy as np

def get_math_value(arr,data,value):
    datas = ['column','row']
    values = ['min','max','mean','median']
    try:
        if(data not in datas or value not in values):
            return  []
        else:        
            i = 0 if data=='column' else 1
            if(value=="min"):
                return np.min(np.array(arr),axis=i)
            elif(value=="max"):
                return np.min(np.array(arr),axis=i)
            elif(value=="mean"):
                return np.mean(np.array(arr),axis=i)
            else:
                return np.median(np.array(arr),axis=i)
    except:
        return []