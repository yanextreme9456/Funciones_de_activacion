import numpy as np #type:ignore
import matplotlib.pyplot as plt

def tanh(x, derivate=False):
    if derivate:
         return 4/(np.exp(x)+np.exp(-x))**2

    else:
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

