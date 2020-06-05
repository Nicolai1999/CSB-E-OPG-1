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

# Parameters for the experiment, interval = [a,b]
a = 0
b = 3

#function to be evaluated
def f(x):
    return x**2-np.sin(10*x)

#plot of the functions and the nodes
#f = red, p_N = green, nodes = blue
for N in range(55,71,5):
    h = abs(b-a)/N      #distance between each points
    x_values = [3*(1-np.cos((j*np.pi)/N))/2 for j in range(N+1)]  #chebysev points 
 #   x_values = [a+j*h for j in range(N+1)]        #equidistant points
    y_values = [f(x_values[k]) for k in range(N+1)]     #nodes = (x_values,y_values)
    x = np.linspace(-1,4,400)    #used to plot the functions
    y1 = lagrange(x,x_values,y_values)                  #x,y1 plots p_N
    y2 = f(x)                                           #x,y2 plots f
    plt.figure()
    plt.title(f"N = {N:}")
    plt.plot(x_values,y_values,"ob",x,y1,"-g",x,y2,"-r")
    plt.axhline(c = 'black', lw = 0.7)   #x-axis
    plt.axvline(c = 'black', lw = 0.7)   #y-axis
    plt.axis([-0,3,-20,20])   #limitation of the axis
    plt.savefig(f"plot_{N:}.png")
