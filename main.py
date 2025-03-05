import matplotlib.pyplot as plt
import numpy as np
from Funciones_de_activación.src.ReLU import relu
from Funciones_de_activación.src.Sigmoid import sigmoid
from Funciones_de_activación.src.Tanh import tanh



def main():
    """
    Plots the ReLU, Tanh, and Sigmoid activation functions along with their derivatives.
    Generates a figure with subplots showing each function and its derivative for a range of input values.
    """
    x=np.linspace(-50,50,500)
    plt.figure()
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    
    #Graph of ReLU function
    plt.subplot(3,2,1)
    plt.plot(x,relu(x))
    plt.title('ReLU')
    plt.grid()
    #Graph of the Tanh function
    plt.subplot(3,2,3)
    plt.plot(x,tanh(x))
    plt.title('Tanh')
    plt.grid()
    #Graph of the sigmoid function
    plt.subplot(3,2,5)
    plt.plot(x,sigmoid(x))
    plt.title('Sigmoid')
    plt.grid()
    
    #Graph of the derived ReLU function
    plt.subplot(3,2,2)
    plt.plot(x,relu(x,True))
    plt.title('Derived ReLU')
    plt.grid()
    
    #Graph of the derived Tanh function
    plt.subplot(3,2,4)
    plt.plot(x,tanh(x,True))
    plt.title('Derived Tanh')
    plt.grid()
    
    #Graph of the derived sigmoid function
    plt.subplot(3,2,6)
    plt.plot(x,sigmoid(x,True))
    plt.title('Derived sigmoid')
    plt.grid()
    
    plt.show()

if __name__=='__main__':
    main()