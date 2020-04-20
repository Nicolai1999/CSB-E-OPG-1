# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from math import sin
import numpy as np

# Interpolating polynomial
def lagrange(x, x_values, y_values): 
    
    from functools import reduce
    # Lagrange basis polynomials
    def l(k,x):
        temp = [(x-x_values[j])/(x_values[k]-x_values[j])\
              for j in range(len(x_values)) if j != k]
        result = reduce(lambda x, y: x*y, temp)
        return result
    
    # Lagrange interpolation polynomial
    p = []
    for i in range(len(x)):
        temp = [y_values[k]*l(k,x[i]) for k in range(len(x_values))]
        p.append(sum(temp))
    return p

# Parameters for the experiment
a = 0
b = 3

def f(x):
    return x**2-np.sin(10*x)

#plot of the functions and the nodes
for N in range(50,81,5):
    h = abs(b-a)/N
    x_values = [a+k*h for k in range(N+1)] 
    y_values = [f(x_values[k]) for k in range(N+1)]     #nodes = (x_values,y_values)
    x = np.linspace(a,b,400)
    y1 = lagrange(x,x_values,y_values)                  #x,y1 plots p_N
    y2 = f(x)                                           #x,y2 plots f
    plt.figure()
    plt.plot(x_values,y_values,"ob",x,y1,"-g",x,y2,"-r")
    plt.savefig(f"plot_{N:}.png")
