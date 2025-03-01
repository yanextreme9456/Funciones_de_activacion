import numpy as np #type:ignore
import matplotlib.pyplot as plt #type:ignore

def relu(x, derivate=False):
      if derivate:
            n=np.array(x)
            n[n>0]=1 
            n[n<=0]=0
            
            return n
      else:
          return np.maximum(0,x)
