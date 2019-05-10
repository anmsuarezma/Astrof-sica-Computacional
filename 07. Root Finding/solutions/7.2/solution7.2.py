'''
Computational Astrophysics 
2019

Solution 7.2
5 order Polynomial root finding 
by the Weierstrass (Druand-Kerner) method
'''

import numpy as np

# Degree of the polynomial
n = 5
a = np.zeros(n+1)

# Define the  here!
# f(x) = a_5 x^5 + a_4 x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0
a[0] = 0.
a[1] = 0.
a[2] = 0.
a[3] = -1.
a[4] = 5.
a[5] = 3.




# Make the polynomial monodic
a[0] = a[0]/a[5]
a[1] = a[1]/a[5]
a[2] = a[2]/a[5]
a[3] = a[3]/a[5]
a[4] = a[4]/a[5]
a[5] = 1.



def f(x):
	return a[5]*x**5 + a[4]*x**4 + a[3]*x**3 + a[2]*x**2 + a[1]*x + a[0]

# Definition of the initial values of the roots

r = np.zeros(n, dtype=np.complex_)
r[0] = complex(1., 0.)
r[1] = complex(0.4, 0.9)
r[2] = complex(0.4, 0.9)**2
r[3] = complex(0.4, 0.9)**3
r[4] = complex(0.4, 0.9)**4

iter=0 # control counter for the Loop

# Main loop of the Weierstrass (Druand-Kerner) method
while True:
	r0 = r[0] - f(r[0])/((r[0] - r[1])*(r[0] - r[2])*(r[0] - r[3])*(r[0] - r[4]))
	r1 = r[1] - f(r[1])/((r[1] - r[0])*(r[1] - r[2])*(r[1] - r[3])*(r[1] - r[4]))
	r2 = r[2] - f(r[2])/((r[2] - r[0])*(r[2] - r[1])*(r[2] - r[3])*(r[2] - r[4]))
	r3 = r[3] - f(r[3])/((r[3] - r[0])*(r[3] - r[1])*(r[3] - r[2])*(r[3] - r[4]))
	r4 = r[4] - f(r[4])/((r[4] - r[0])*(r[4] - r[1])*(r[4] - r[2])*(r[4] - r[3]))

	r[0] = r0
	r[1] = r1
	r[2] = r2
	r[3] = r3
	r[4] = r4
	
	iter = iter + 1

	# stop the loop when zeros are met
	if(sum(abs(f(r)))<= 1e-13):
		break

	# control stop at 1000 iterations
	if(iter>1000):
		break


# Print the results
print()
print("--------------------------------------------------------------")
print("\nThe roots of the polynomial are:\n")
print()
tol = 1e-4
for i in range(n):
	if abs(r[i].real) <= tol and abs(r[i].imag) <= tol:
		print("r",i+1," = ", 0.0, "   (zero root)")
		print("f(r1) = ", f(0.))
		print("--------------------------------------------------------------")
		print()
	elif abs(r[i].imag) <= tol:
		print("r",i+1," = ", r[i].real, "   (real root)")
		print("f(r) = ", f(r[i].real))
		print("--------------------------------------------------------------")			
		print()
	elif abs(r[i].real) <= tol:
		print("r",i+1," = ", r[i].imag, "j", "   (imaginary root)")
		print("f(r) = ", f(r[i].imag))
		print("--------------------------------------------------------------")
		print()
	else:
		print("r",i+1," = ", r[i], "   (complex root)")
		print("f(r) = ", f(r[i]))
		print("--------------------------------------------------------------")
		print()


print(" Number of iterations: ", iter, "\n")



