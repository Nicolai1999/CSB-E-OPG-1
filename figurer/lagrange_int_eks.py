import numpy as np
import matplotlib.pyplot as plt


def fun(x):
    return -3*(x-1)*(x-3)+4*(x-1)*(x-2)

p_x = np.array([1, 2, 3])
p_y = fun(p_x)
x = np.linspace(-5, 5, 1000)
y = fun(x)

plt.grid(True)
plt.ylim(-2, 10)
plt.xlim(-4, 4)

plt.plot(x, y, color = 'black')
plt.scatter(p_x, p_y, c = 'black')

