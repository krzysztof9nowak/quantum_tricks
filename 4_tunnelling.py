import numpy as np
import scipy
from findiff import FinDiff
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.sparse.linalg import spsolve

### PROPERTIES OF A PARTICLE AND PHYSICS CONSTANTS ####
m = 1
v = 50
starting_pos = -0.6
sigma_pos = 0.1
hbar = 1
#######################################################


n = 10000
x = np.linspace(-1, 1, n)
dx = x[1] - x[0]

V = np.full(x.shape, 0.0)
V[4800 : 5200] = 2e3

d2_dx2 = FinDiff(0, dx, 2, acc=2)
H = - 0.5 * hbar**2 / m * d2_dx2.matrix(x.shape) + scipy.sparse.diags(V)

mag = lambda x: (x * np.conj(x)).real
normalize = lambda x: x / np.sum(x)


def gauss_x(x, a, x0, k):
    """a gaussian wave packet of width a, centered at x0, with wave vector k0""" 
    return np.exp(-(x-x0)**2/2/a**2)*np.exp(1j*k*x)


k = m*v / hbar
print(k)
psi = gauss_x(x, sigma_pos, starting_pos, k)

dt = 0.0005

fig, ax_x = plt.subplots()
ax_u = ax_x.twinx()
ax_u.plot(x, V, color='black', linewidth=2)
ax_u.set_ylabel("U(x)")
line_psi, = ax_x.plot(x, normalize(mag(psi)), color='crimson')
ax_x.set_ylabel('$\Psi^2(x)$', color='crimson')
ax_x.set_xlabel('x')
ax_x.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
ax_x.set_ylim(-1e-4, 2e-3)

bck = (-H * dt / (2j * hbar)) + scipy.sparse.identity(H.shape[0])
fwd = (H * dt / (2j * hbar)) + scipy.sparse.identity(H.shape[0])

def update(t):
    print(t)
    global psi
    psi = spsolve(bck, fwd.dot(psi))
    line_psi.set_ydata(normalize(mag(psi)))

ani = FuncAnimation(fig, update, 60, interval=100)
writer = PillowWriter(fps=10)  
ani.save("4_tunnelling_50.gif", writer=writer)  

plt.show()
