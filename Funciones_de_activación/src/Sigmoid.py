import numpy as np #type:ignore
import matplotlib.pyplot as plt
def sigmoid(x, derivate=False):
      """
      Computes the sigmoid activation function, which maps input values to a range between 0 and 1.
      If the derivative flag is True, it returns the derivative of the sigmoid function, representing the slope at each point.
      """
      if derivate:
          return np.exp(-x)/(np.exp(-x)+1)**2
      else:
          return 1/(1+np.exp(-x))

