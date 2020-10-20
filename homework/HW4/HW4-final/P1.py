import numpy as np
from numpy import log as ln
import matplotlib.pyplot as plt

def numerical_diff(f, h):
    def inner(x):
        return (f(x + h) - f(x)) / h
    return inner

x_list = np.arange(0.2, 0.4, 0.01)
h_list = [1E-1, 1E-7, 1E-15]
deriv = 1 / x_list

firstObj = numerical_diff(ln, h_list[0])
y1 = firstObj(x_list)

secondObj = numerical_diff(ln, h_list[1])
y2 = secondObj(x_list)

thirdObj = numerical_diff(ln, h_list[2])
y3 = thirdObj(x_list)

fig, ax = plt.subplots(1, 1, figsize=(10,6), constrained_layout = True)
ax.set_xlabel(r'$x$', 
              fontsize = 16)
ax.set_ylabel(r'$derivative$', 
              fontsize = 16)
ax.set_title(r'Comparing finite difference to true derivative', 
             fontsize = 16)
ax.plot(x_list, y1, label = r'$f_{FD}(x)$ for h = $1 x 10^{-1}$')
ax.plot(x_list, y2, label = r'$f_{FD}(x)$ for h = $1 x 10^{-7}$')
ax.plot(x_list, y3, label = r'$f_{FD}(x)$ for h = $1 x 10^{-15}$')
ax.plot(x_list, deriv,'--', label = 'Analytical Derivative')
ax.legend(fontsize = 16)

plt.savefig('P1_fig.png')
