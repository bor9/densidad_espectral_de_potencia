__author__ = 'ernesto'

import numpy as np
import matplotlib.pyplot as plt


# sigmoide 1
step = 0.01
xmin = -5
xmax = 10
beta = 8
amp = 2
x = np.arange(xmin, xmax, step)
s = amp*(1/(1.+np.exp(-1*beta*(x-xmin)))+1/(1.+np.exp(-1*beta*(x-xmax)))-1/2)
plt.figure()
plt.plot(x, s, 'k-')
plt.show()

# sigmoide 2
step = 0.01
xmin = -5
xmax = 10
beta = 8
amp = 2
y = 10

# def curly_brace(xmin, xmax, y, amp, beta=8, step=0.01)

xm = (xmin+xmax)/2
x_left = np.arange(xmin, xm, step)
hb_left = amp*(1/(1.+np.exp(-1*beta*(x_left-xmin)))+1/(1.+np.exp(-1*beta*(x_left-xm)))-1/2+y)
x = np.concatenate((x_left, np.arange(xm, xmax-step, step)))
hb = np.concatenate((hb_left, hb_left[-2::-1]))
print(xm)
print(x_left[-1])
print(x.shape)
print(hb.shape)
print(hb[0])
print(hb[-1])
plt.figure()
plt.plot(x, hb, 'k.')
plt.show()
