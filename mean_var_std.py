import numpy as np

#[0,1,2,3,4,5,6,7,8]
def calculate(list):
    if len(list) == 9:
        # reshape list, initialize dict
        reshaped_arr = np.array(list).reshape(3,3)
        calculations = {'mean':[], 'variance':[], 'standard deviation':[], 'min':[], 'max':[], 'sum':[]}

        # add values to dict for axis 0, axis 1 and no axis
        for ax in (0,1, None):
            calculations['mean'] += [reshaped_arr.mean(axis=ax).tolist()]
            calculations['variance'] += [reshaped_arr.var(axis=ax).tolist()]
            calculations['standard deviation'] += [reshaped_arr.std(axis=ax).tolist()]
            calculations['min'] += [reshaped_arr.min(axis=ax).tolist()]
            calculations['max'] += [reshaped_arr.max(axis=ax).tolist()]
            calculations['sum'] += [reshaped_arr.sum(axis=ax).tolist()]
        
        return calculations
        
    else:
        raise ValueError("List must contain nine numbers.")  
