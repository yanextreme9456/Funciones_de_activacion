import matplotlib.pyplot as plt
import numpy as np
from Funciones_de_activación.src.ReLU import relu
from Funciones_de_activación.src.Sigmoid import sigmoid
from Funciones_de_activación.src.Tanh import tanh



def main():
    x=np.linspace(-50,50,500)
    plt.figure()
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    
    #Gráfica de la funcion ReLU
    plt.subplot(3,2,1)
    plt.plot(x,relu(x))
    plt.title('ReLU')
    plt.grid()
    #Gráfica de la funcion Tanh
    plt.subplot(3,2,3)
    plt.plot(x,tanh(x))
    plt.title('Tanh')
    plt.grid()
    #Gráfica de la funcion sigmoide
    plt.subplot(3,2,5)
    plt.plot(x,sigmoid(x))
    plt.title('Sigmoide')
    plt.grid()
    
    #Gráfica de la funcion ReLU derivada
    plt.subplot(3,2,2)
    plt.plot(x,relu(x,True))
    plt.title('ReLU derivada')
    plt.grid()
    
    #Gráfica de la funcion Tanh derivada
    plt.subplot(3,2,4)
    plt.plot(x,tanh(x,True))
    plt.title('Tanh derivada')
    plt.grid()
    
    #Gráfica de la funcion sigmoide derivada
    plt.subplot(3,2,6)
    plt.plot(x,sigmoid(x,True))
    plt.title('Sigmoide derivada')
    plt.grid()
    
    plt.show()

if __name__=='__main__':
    main()