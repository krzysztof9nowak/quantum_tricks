import numpy as np
import scipy
from findiff import FinDiff
import matplotlib.pyplot as plt
import time

def measure(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print('Time needed for %s: %10.2f seconds.' % (func.__name__, stop - start))
        return result
        
    return wrapper

@measure
def build_grid(box_size, npoints):
    x = y = z = np.linspace(-box_size/2, box_size/2, npoints)
    dx = dy = dz = x[1] - x[0]
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    return (x, y, z), (dx, dy, dz), (X, Y, Z)

@measure
def build_hamiltionian(X, Y, Z, acc=2):    
    dx = dy = dz = X[1, 0, 0] - X[0, 0, 0]
    # V = 0.5 * (X**2 + Y**2 + Z**2)
    V = -1  / (4*np.pi * np.sqrt((X**2 + Y**2 + Z**2))) # atom
    # plt.plot(V[10,10, :])
    # plt.show()
    V = scipy.sparse.diags(V.reshape(-1))
    laplace = FinDiff(0, dx, 2, acc=acc) + FinDiff(1, dy, 2, acc=acc) + FinDiff(2, dz, 2, acc=acc)
    T = -0.5 * laplace.matrix(X.shape)
    H = T + V
    return H, T, V

@measure
def solve(H, k):
    spectrum, states = scipy.sparse.linalg.eigs(H, which='SR', k=k)
    return spectrum, states

@measure
def run(box_size, npoints, acc=2):
    (x, y, z), (dx, dy, dz), (X, Y, Z) = build_grid(box_size, npoints)
    H, T, V = build_hamiltionian(X, Y, Z, acc)
    spectrum, states = solve(H, k=1) #12
    print(spectrum)
    # print('Error in ground state energy: %12.4f' % (spectrum[0].real - 1.5))
    return states[:, 0].reshape((npoints, npoints, npoints, ))
    
mag = lambda x: (x * np.conj(x)).real
solution = run(box_size=0.1, npoints=20, acc=2)
sol_mag = mag(solution)
# plt.plot(sol_mag[5, 5, :])
plt.plot(sol_mag[10, 10, :])
plt.show()