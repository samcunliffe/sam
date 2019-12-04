from sam.pp.kinematics.two_body_phsp import two_body_phsp_q
from math import sqrt
import numpy as np
import matplotlib.pyplot as pp
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 


MASSB0 = 5279.64

def mmumu(qsq):
    """the dimuon invariant mass from a qsq value"""
    return sqrt(qsq)*1000.

def qsq_kinematic(mkpi):
    """the y (qsq) values at the kinematic edge as a function of mkpi"""
    return 

mkpi_vals = np.arange(634, 1200, 1)
qsq_vals = np.arange(0.1, 19, 0.1)



mmumu_vals = [ mmumu(qsq) for qsq in qsq_vals ]
X, Y = np.meshgrid(mkpi_vals, mmumu_vals)

func = np.vectorize(two_body_phsp_q)

Z = func(MASSB0, X, Y)

fig = pp.figure()
ax = Axes3D(fig) #<-- Note the difference from your original code...
#ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,# cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
#fig.colorbar(surf, shrink=0.5, aspect=5)

pp.savefig("hello.pdf")

