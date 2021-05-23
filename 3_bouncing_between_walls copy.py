import numpy as np
import scipy
from findiff import FinDiff
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.sparse.linalg import spsolve
from scipy.fftpack import fft,ifft

########## PROPERTIES OF PARTICLE AND PHYSICS
m = 1
v = 60
hbar = 1

##############################################


n = 1000
x = np.linspace(-1, 1, n)
dx = x[1] - x[0]
ks = 2 * np.pi * x / n / (dx**2)


V = np.full(x.shape, 0.0)
# V[:500] = 1e4
# V[9500:] = 1e4
# V[4800 : 5200] = 2e3

d2_dx2 = FinDiff(0, dx, 2, acc=2)
H = - 0.5 * hbar**2 / m * d2_dx2.matrix(x.shape) + scipy.sparse.diags(V)

mag = lambda x: (x * np.conj(x)).real
normalize = lambda x: x / np.linalg.norm(x)


def gauss_x(x, a, x0, k):
    """a gaussian wave packet of width a, centered at x0, with wave vector k0""" 
    return normalize(np.exp(-(x-x0)**2/2/a**2)*np.exp(1j*k*x))


k = m*v / hbar
print(k)
psi = gauss_x(x, 0.1, 0.5, k)

dt = 0.0005
ts = np.arange(0, 0.1, dt)


fig, ax_x = plt.subplots(1)
line_psi, = ax_x.plot(x, mag(psi), color='crimson')
# line_psi, = ax.plot(x, np.real(psi))
# line_psi2, = ax.plot(x, np.imag(psi))
ax_u = ax_x.twinx()
ax_u.plot(x, V, color='black')



bck = (-1j * H * dt / 2) + scipy.sparse.identity(H.shape[0])
fwd = (1j * H * dt / 2) + scipy.sparse.identity(H.shape[0])

def update(t):
    global psi
    psi = spsolve(bck, fwd.dot(psi))
    line_psi.set_ydata(mag(psi))
    # line_psi.set_ydata(np.real(psi))
    # line_psi2.set_ydata(np.imag(psi))


ani = FuncAnimation(fig, update, ts, interval=100)
plt.show()
