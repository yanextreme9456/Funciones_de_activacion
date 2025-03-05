import numpy as np #type:ignore
import matplotlib.pyplot as plt #type:ignore

def relu(x, derivate=False):
      """
      Computes the ReLU activation function, which returns the input if it is positive, otherwise returns zero.
      If the derivative flag is True, it returns a binary mask where positive inputs are 1 and non-positive inputs are 0.
      """
      if derivate:
            n=np.array(x)
            n[n>0]=1 
            n[n<=0]=0
            
            return n
      else:
          return np.maximum(0,x)
