import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

def gaussian(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

# Clean data
X = np.linspace(15, 21, 100)
Y = gaussian(X, 0.65, 17.6, 1.)

# Noisy dat
Xn = np.random.uniform(16, 20, 25)
Yn = gaussian(Xn, 0.65, 17.6, 1.) + 0.01 * np.random.normal(size=len(Xn))


C = np.empty((len(X),2))
C[:,0] = X
C[:,1] = Y
np.savetxt("curve.csv", C, delimiter=",")

P = np.empty((len(Xn),2))
P[:,0] = Xn
P[:,1] = Yn
np.savetxt("points.csv", P, delimiter=",")
