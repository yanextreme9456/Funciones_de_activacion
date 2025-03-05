import numpy as np #type:ignore
import matplotlib.pyplot as plt

def tanh(x, derivate=False):
    """
    Computes the hyperbolic tangent (tanh) activation function, which maps input values to a range between -1 and 1.
    If the derivative flag is True, it returns the derivative of the tanh function, representing the slope at each point.
    """
    if derivate:
         return 4/(np.exp(x)+np.exp(-x))**2

    else:
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

