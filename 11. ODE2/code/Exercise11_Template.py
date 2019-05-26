'''
Computational Astrophysics 
2019

Exercise 11
Boundary Value Problem (BVP) Template
'''
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Set up the grid
xmin = 0.0
xmax = 1.0
npoints = 1000
x = np.linspace(xmin,xmax,npoints)
dx = x[1]-x[0]

# Boundary conditions
A = 0.0 # inner boundary
B = 0.1 # outer boundary

def ODE_rhs(u,xx):
    
    rhs = np.zeros(2)
    rhs[0] = u
    rhs[1] = 12.0*xx - 4.0

    return rhs

def integrate_FE(z,x):

    # Define an array for all points
    # Entry 0 contains y
    # Entry 1 contains y'
    yy = np.zeros((npoints,2))

    # Initial values
    yy[0,0] = A
    yy[0,1] = z

    for i in range(npoints-1):
        yy[i+1,:] = yy[i,:] + dx*ODE_rhs(yy[i,1],x[i])

    return yy

# Give initial guess for the derivative
z0 = -1100000.0
z1 = -10000000.0
yy0 = integrate_FE(z0,x)
yy1 = integrate_FE(z1,x)
phi0 = yy0[npoints-1,0] - B
phi1 = yy1[npoints-1,0] - B
dphidz = (phi1-phi0)/(z1-z0)

i = 0
itmax = 100
err = 1.0e99
criterion = 1.0e-12

z0 = z1
phi0 = phi1
while (err > 1.0e-12 and i < itmax):
    z1 = z0 - phi0 * 1.0 / dphidz
    yy = integrate_FE(z1,x)
    phi1 = yy[npoints-1,0] - B
    dphidz = (phi1 - phi0) / (z1-z0)
    err = np.abs(phi1)
    z0 = z1
    phi0 = phi1
    i = i+1

    print i,z1,phi1

plt.plot(x,yy[:,0],"r-")
plt.plot(x,2.0*x**3 - 2*x**2 + 0.1*x,"k-")
#plt.plot(x,yy2[:,0],"b-")
#plt.plot(x,yy3[:,0],"g-")
plt.show()




