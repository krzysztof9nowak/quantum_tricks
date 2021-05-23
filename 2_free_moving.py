import numpy as np
import scipy
from findiff import FinDiff
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.sparse.linalg import spsolve
from scipy.fftpack import fft,ifft

### PROPERTIES OF A PARTICLE AND PHYSICS CONSTANTS ####
m = 1
v = 30
starting_pos = -0.6
sigma_pos = 0.1
hbar = 1
#######################################################


n = 1000
x = np.linspace(-1, 1, n)
dx = x[1] - x[0]
ks = 2 * np.pi * x / n / (dx**2)


V = np.full(x.shape, 0.0)
d2_dx2 = FinDiff(0, dx, 2, acc=2)
H = - 0.5 * hbar**2 / m * d2_dx2.matrix(x.shape) + scipy.sparse.diags(V)

mag = lambda x: (x * np.conj(x)).real
normalize = lambda x: x / np.linalg.norm(x)


def gauss_x(x, a, x0, k):
    """a gaussian wave packet of width a, centered at x0, with wave vector k0""" 
    return normalize(np.exp(-(x-x0)**2/2/a**2)*np.exp(1j*k*x))


k = m*v / hbar
print(k)
psi = gauss_x(x, sigma_pos, starting_pos, k)

dt = 0.0005

fig, ax_x = plt.subplots()
line_psi, = ax_x.plot(x, mag(psi), color='crimson')
ax_x.set_ylabel('$\Psi^2(x)$', color='crimson')
ax_x.get_xaxis().set_visible(False)
ax_x.tick_params(left=False, labelleft=False)
# line_psi, = ax_x.plot(x, np.real(psi))
# line_psi2, = ax_x.plot(x, np.imag(psi))



bck = (-H * dt / (2j * hbar)) + scipy.sparse.identity(H.shape[0])
fwd = (H * dt / (2j * hbar)) + scipy.sparse.identity(H.shape[0])

def update(t):
    print(t)
    global psi
    psi = spsolve(bck, fwd.dot(psi))
    line_psi.set_ydata(mag(psi))
    # line_psi.set_ydata(np.real(psi))
    # line_psi2.set_ydata(np.imag(psi))


ani = FuncAnimation(fig, update, 60, interval=100)
writer = PillowWriter(fps=10)  
ani.save("2_free.gif", writer=writer)  

plt.show()
