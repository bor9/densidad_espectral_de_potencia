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


T = 10
t_max = T+2
tau1 = T/2 + 1.5
tau2 = -T/2 + 2
dtau = T/15

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
plt.text(t_max, -0.8, r'$t_1$', fontsize=font_size2, ha='right', va='center')
plt.text(ytm, t_max, r'$t_2$', fontsize=font_size2, ha='left', va='top')

# rectangle
plt.plot([-T/2, T/2], [T/2, T/2], 'k')
plt.plot([-T/2, T/2], [-T/2, -T/2], 'k')
plt.plot([-T/2, -T/2], [-T/2, T/2], 'k')
plt.plot([T/2, T/2], [-T/2, T/2], 'k')

# stripes
# positive tau
# dashed lines
# Equation: x(t_1) = t_1 + tau
ti1 = -T-2
plt.plot([ti1, 0], [ti1+tau1, tau1], 'k--', dashes=(5, 3))
plt.plot([ti1, 0], [ti1+tau1+dtau, tau1+dtau], 'k--', dashes=(5, 3))
#
plt.plot([-T/2, T/2-tau1], [-T/2+tau1, T/2], 'k-')
plt.plot([-T/2, T/2-tau1-dtau], [-T/2+tau1+dtau, T/2], 'k-')
# filled area with a polygon patch
# vertices
vertices1 = np.array([[-T/2, -T/2+tau1], [-T/2, -T/2+tau1+dtau], [T/2-tau1-dtau, T/2], [T/2-tau1, T/2]])
ax.add_patch(Polygon(vertices1, color='#CCCCCC'))

# negative tau
# dashed lines
ti2 = -T+2
ti3 = T/2
plt.plot([ti2, ti3], [ti2+tau2, ti3+tau2], 'k--', dashes=(5, 3))
plt.plot([ti2, ti3], [ti2+tau2+dtau, ti3+tau2+dtau], 'k--', dashes=(5, 3))
#
plt.plot([-T/2-tau2, ti3], [-T/2, ti3+tau2], 'k-')
plt.plot([-T/2-tau2-dtau, ti3], [-T/2, ti3+tau2+dtau], 'k-')
# vertices
vertices2 = np.array([[-T/2-tau2, -T/2], [ti3, ti3+tau2], [ti3, ti3+tau2+dtau], [-T/2-tau2-dtau, -T/2]])
ax.add_patch(Polygon(vertices2, color='#CCCCCC'))

# yticks
plt.plot([0, tl], [T, T], 'k-')
plt.plot([0, tl], [-T, -T], 'k-')
plt.plot([0, tl], [tau1, tau1], 'k-')
plt.plot([0, tl], [tau2, tau2], 'k-')
plt.plot([0, tl], [tau1+dtau, tau1+dtau], 'k-')
plt.plot([0, tl], [tau2+dtau, tau2+dtau], 'k-')
# ylabels
plt.text(ytm, T, r'$T$', fontsize=font_size2, ha='left', va='center')
plt.text(ytm, -T, r'$-T$', fontsize=font_size2, ha='left', va='center')
plt.text(ytm, tau1, r'$\tau$', fontsize=font_size2, ha='left', va='center')
plt.text(ytm, tau2, r"$\tau'$", fontsize=font_size2, ha='left', va='center')
plt.text(ytm, tau1+dtau, r'$\tau+\Delta\tau$', fontsize=font_size2, ha='left', va='center')
plt.text(-ytm, tau2+dtau, r"$\tau'+\Delta\tau$", fontsize=font_size2, ha='right', va='center')

# rects labels fot tau > 0
plt.text(ti1, ti1+tau1+0.4, r'$t_2-t_1=\tau$', fontsize=font_size2, rotation=45, ha='left', va='center')
plt.text(ti1, ti1+tau1+dtau+2.5, r'$t_2-t_1=\tau+\Delta\tau$', fontsize=font_size2, rotation=45, ha='left', va='center')
# rects labels fot tau < 0
plt.text(ti2, ti2+tau2+0.8, r"$t_2-t_1=\tau'<0$", fontsize=font_size2, rotation=45, ha='left', va='center')

# others rects labels
x1, b1 = curly_brace(-(tau1-T/2), 0, T/2-1, 0.5, position='down', beta=20, step=0.01)
plt.plot(x1, b1, 'k')
plt.text(-(tau1-T/2)/2, T/2-2.1, r"$\tau-\frac{T}{2}$", fontsize=font_size2, ha='center', va='center')

x2, b2 = curly_brace(-T/2, -(tau1-T/2), T/2+1.5, 0.5, position='up', beta=20, step=0.01)
plt.plot(x2, b2, 'k')
plt.text((-tau1+T/2-T/2)/2, T/2+2.6, r"$\frac{T}{2}-\left(\tau-\frac{T}{2}\right)=T-\tau$", fontsize=font_size2,
         ha='center', va='center')

plt.text(-2, 2, r"$\sqrt{2}(T-\tau)$", fontsize=font_size2, ha='center', va='center')

# trapezoid heigh
plt.plot([-T/2, -T/2+dtau/2], [-T/2+tau1+dtau, -T/2+dtau/2+tau1], 'k')

ax.annotate(r"$\Delta\tau/\sqrt{2}$", xy=((-T+dtau/2)/2, (-T+3*dtau/2+2*tau1)/2), xycoords='data', xytext=(-T+3, 5), textcoords='data',
            va="center", ha="right", fontsize=font_size2,
            arrowprops=dict(arrowstyle="->", color="k", shrinkA=25, shrinkB=1, patchA=None,
                            patchB=None, connectionstyle="angle3,angleA=0,angleB=70"))


# rotated curly brace
x3, b3 = curly_brace(0, np.sqrt(2)*(T-tau1), 0, 0.5, position='down', beta=20, step=0.01)
x3_rot = np.sqrt(np.square(x3)+np.square(b3))*np.sin(np.pi/4-np.arctan(b3/x3))
b3_rot = np.sqrt(np.square(x3)+np.square(b3))*np.cos(np.pi/4-np.arctan(b3/x3))
x3_rot -= T/2-0.2
b3_rot += tau1-T/2-0.2
plt.plot(x3_rot, b3_rot, 'k')

# ylabels
plt.text(ytm, T/2+0.1, r'$T/2$', fontsize=font_size2, ha='left', va='bottom')
plt.text(ytm, -T/2-0.1, r'$-T/2$', fontsize=font_size2, ha='left', va='top')
plt.text(-T/2+0.2, -0.2, r'$-T/2$', fontsize=font_size2, ha='left', va='top')
plt.text(T/2+0.2, -0.2, r'$T/2$', fontsize=font_size2, ha='left', va='top')


plt.axis('off')
plt.savefig('wiener_khintchine_integration_v2.eps', format='eps', bbox_inches='tight')
plt.show()
