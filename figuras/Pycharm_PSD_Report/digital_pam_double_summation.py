import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib import rc

__author__ = 'ernesto'

# if use latex or mathtext
rc('text', usetex=False)


def curly_brace(xmin, xmax, y, amp, position='up', beta=8, step=0.01):
    xm = (xmin+xmax)/2
    x_left = np.arange(xmin, xm, step)
    hb_left = amp*(1/(1.+np.exp(-1*beta*(x_left-xmin)))+1/(1.+np.exp(-1*beta*(x_left-xm)))-1/2)
    x = np.concatenate((x_left, np.arange(xm, xmax-step, step)))
    hb = np.concatenate((hb_left, hb_left[-2::-1]))
    if position == 'up':
        return x, hb+y
    elif position == 'down':
        return x, -hb+y
    elif position == 'left':
        return hb, x
    elif position == 'right':
        return -hb, x

K = 6
M = K * 2
t_max = M+2
n1 = 9
n2 = -4
dtau = M/15

# ticks length
tl = t_max/40
# y tick margin
ytm = 0.6
# font size
font_size1 = 18
font_size2 = 12

fig = plt.figure(1, figsize=(8, 8), frameon=False)
ax = fig.add_subplot(111)
plt.ylim(-t_max, t_max)
plt.xlim(-t_max, t_max)

# axis arrows
plt.annotate("", xytext=(-t_max, 0), xycoords='data', xy=(t_max, 0), textcoords='data',
             arrowprops=dict(width=0.2, headwidth=6, headlength=8, facecolor='black', shrink=0.002))
plt.annotate("", xytext=(0, -t_max), xycoords='data', xy=(0, t_max), textcoords='data',
             arrowprops=dict(width=0.2, headwidth=6, headlength=8, facecolor='black', shrink=0.002))

# axis labels
plt.text(t_max, -0.8, r'$m$', fontsize=font_size2, ha='right', va='center')
plt.text(ytm, t_max, r'$k$', fontsize=font_size2, ha='left', va='top')

# positive tau
# dashed lines
# Equation: x(t_1) = t_1 + tau
ti1 = -M
plt.plot([ti1, 0], [ti1+n1, n1], 'r--', dashes=(5, 3))

# negative tau
# dashed lines
ti2 = -M+5
ti3 = M/2
plt.plot([ti2, ti3], [ti2+n2, ti3+n2], 'b--', dashes=(5, 3))

# rectangle of points
index = np.arange(-K, K+1)
for i in index:
    plt.plot(i*np.ones(2*K+1), index, 'k.', markersize=8)

# yticks
plt.plot([0, tl], [K, K], 'k-')
plt.plot([0, tl], [-K, -K], 'k-')
plt.plot([0, tl], [M, M], 'k-')
plt.plot([0, tl], [-M, -M], 'k-')
plt.plot([0, tl], [n1, n1], 'r-')
plt.plot([0, tl], [n2, n2], 'b-')
# ylabels
plt.text(ytm, M, r'$2K$', fontsize=font_size2, ha='left', va='center')
plt.text(ytm, -M, r'$-2K$', fontsize=font_size2, ha='left', va='center')
plt.text(ytm, n1, r'$n$', fontsize=font_size2, ha='left', va='center', color='red')
plt.text(-ytm/3, n2+0.3, r"$n'$", fontsize=font_size2, ha='right', va='center', color='blue')
plt.text(ytm, K+0.1, r'$K$', fontsize=font_size2, ha='left', va='bottom')
plt.text(ytm, -K-0.2, r'$-K$', fontsize=font_size2, ha='left', va='top')

# xticks
plt.plot([K, K], [0, tl], 'k-')
plt.plot([-K, -K], [0, tl], 'k-')
# xlabels
plt.text(-K-0.2, 0.2, r'$-K$', fontsize=font_size2, ha='right', va='baseline')
plt.text(K+0.2, 0.2, r'$K$', fontsize=font_size2, ha='left', va='baseline')


# rects labels fot tau > 0
plt.text(ti1, ti1+n1+0.4, r'$k-m=n$', fontsize=font_size2, rotation=45, ha='left', va='center', color='red')
# rects labels fot tau < 0
plt.text(ti2, ti2+n2+0.8, r"$k-m=n'<0$", fontsize=font_size2, rotation=45, ha='left', va='center', color='blue')

# curly brace
x1, b1 = curly_brace(-K, -(n1-K), K+2.5, 0.5, position='up', beta=20, step=0.02)
plt.plot(x1, b1, 'k')
plt.text((-n1+K-K)/2, K+4.6, r"$-(n-K)-(-K)+1=$", fontsize=font_size2,
         ha='center', va='center')
plt.text((-n1+K-K)/2, K+3.6, r"$2K-n+1$", fontsize=font_size2,
         ha='center', va='center')

# positive n annotations
ax.annotate(r"$-K$", xy=(-K, K), xycoords='data', xytext=(-K-2, K+1),
            textcoords='data', va="center", ha="right", fontsize=font_size2,
            arrowprops=dict(arrowstyle="->", color="k", shrinkA=15, shrinkB=3, patchA=None,
                            patchB=None, connectionstyle="angle3,angleA=0,angleB=140"))

ax.annotate(r"$-(n-K)$", xy=(-(n1-K), K), xycoords='data', xytext=(-K-2, K+2),
            textcoords='data', va="center", ha="right", fontsize=font_size2,
            arrowprops=dict(arrowstyle="->", color="k", shrinkA=30, shrinkB=3, patchA=None,
                            patchB=None, connectionstyle="angle3,angleA=0,angleB=140"))

# negative n annotations
ax.annotate(r"$-(n'+K)$", xy=(-(n2+K), -K), xycoords='data', xytext=(-(n2+K)+0.2, -K-4),
            textcoords='data', va="center", ha="center", fontsize=font_size2,
            arrowprops=dict(arrowstyle="->", color="k", shrinkA=10, shrinkB=3, patchA=None,
                            patchB=None, connectionstyle="angle3,angleA=90,angleB=140"))

# negative n annotations
ax.annotate(r"$K$", xy=(K, -K), xycoords='data', xytext=(K+0.2, -K-2),
            textcoords='data', va="center", ha="center", fontsize=font_size2,
            arrowprops=dict(arrowstyle="->", color="k", shrinkA=10, shrinkB=3, patchA=None,
                            patchB=None, connectionstyle="angle3,angleA=90,angleB=140"))


plt.axis('off')
plt.savefig('digital_pam_double_summation.eps', format='eps', bbox_inches='tight')
plt.show()
