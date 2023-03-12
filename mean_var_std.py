import numpy as np

def calculate(list):
  
  
  if len(list) < 9:
    
    raise ValueError("List must contain nine numbers.")
  else:
    
    matrix = np.array(list)
    #print(matrix)
    shape = (3,3)
    matrix = matrix.reshape(shape)
    #print(matrix)
    matrix_flatten = matrix.flatten()
       
        #calculations = matrix
        #Criação lista mean
    list_mean = [[matrix[:,0].mean(),matrix[:,1].mean(), matrix[:,2].mean()], 
                [matrix[0,:].mean(),matrix[1,:].mean(), matrix[2,:].mean()],
                matrix_flatten.mean()]
        #print(list_mean)
        #criação lista variância 
    list_var = [[np.var(matrix[:,0]),np.var(matrix[:,1]),np.var(matrix[:,2])],
                    [np.var(matrix[0,:]),np.var(matrix[1,:]), np.var(matrix[2,:])],  
                    np.var(matrix_flatten)]
         #criação lista std deviation 
    list_std_deviation = [[np.std(matrix[:,0]),np.std(matrix[:,1]), np.std(matrix[:,2])],
                             [np.std(matrix[0,:]), np.std(matrix[1,:]), np.std(matrix[2,:])],
                             [np.std(matrix_flatten)]]
        #criação lista max
    list_max = [[np.max(matrix[:,0]),np.max(matrix[:,1]), np.max(matrix[:,2])],
                   [np.max(matrix[0,:]), np.max(matrix[1,:]), np.max(matrix[2,:])],
                   [np.max(matrix_flatten)]]
        #criação lista min
    list_min = [[np.min(matrix[:,0]),np.min(matrix[:,1]), np.min(matrix[:,2])],
                   [np.min(matrix[0,:]), np.min(matrix[1,:]), np.min(matrix[2,:])],
                   [np.min(matrix_flatten)]]
        #criação lista sum
    list_sum = [[np.sum(matrix[:,0]),np.sum(matrix[:,1]), np.sum(matrix[:,2])],
                   [np.sum(matrix[0,:]), np.sum(matrix[1,:]), np.sum(matrix[2,:])],
                   [np.sum(matrix_flatten)]]
        
        
        
        
    calculations = {
            
            'mean': list_mean,
            'variance': list_var,
            'standard deviation': list_std_deviation,
            'max': list_max,
            'min': list_min,
            'sum': list_sum
        
        }
           

    
    
    
  
    
    
    
    
    
    
  return calculations
    
    
    
    
    