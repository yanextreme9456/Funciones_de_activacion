import numpy as np

def relu(x, derivate=False):
      if derivate:
          x[x<=0]=0
          x[x>0]=1
          return x
      else:
          return np.maximum(0,x)