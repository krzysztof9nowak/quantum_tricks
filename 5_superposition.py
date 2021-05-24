import numpy as np
import scipy
from findiff import FinDiff
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.sparse.linalg import spsolve

### PROPERTIES OF A PARTICLE AND PHYSICS CONSTANTS ####
m = 1
hbar = 1
#######################################################


n = 1000
x = np.linspace(-1, 1, n)
dx = x[1] - x[0]
d2_dx2 = FinDiff(0, dx, 2, acc=2)

V = np.full(x.shape, 1e9)
V[50 : 950] = 0.0

H = - 0.5 * hbar**2 / m * d2_dx2.matrix(x.shape) + scipy.sparse.diags(V)
spectrum, states = scipy.sparse.linalg.eigs(H, which='SR', k=3)

psi = 1/np.sqrt(2)*(states[:, 1] + states[:, 0])

mag = lambda x: (x * np.conj(x)).real
normalize = lambda x: x / np.sum(x)

dt = 0.02

fig, (ax_x, ax_mag) = plt.subplots(2)

ax_x.get_xaxis().set_visible(False)
ax_x.tick_params(left=False, labelleft=False)
line_psi, = ax_x.plot(x, np.real(psi), label='Re')
line_psi2, = ax_x.plot(x, np.imag(psi), label='Im')
ax_x.set_ylabel('$\Psi(x)$')
ax_x.legend(loc='upper right')
ax_x.set_ylim(-7e-2, 7e-2)



ax_mag.set_ylabel('$\Psi^2(x)$', color='crimson')
line_psi_mag, = ax_mag.plot(x, normalize(mag(psi)), color='crimson')
ax_mag.set_xlabel('x')
ax_mag.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)


bck = (-H * dt / (2j * hbar)) + scipy.sparse.identity(H.shape[0])
fwd = (H * dt / (2j * hbar)) + scipy.sparse.identity(H.shape[0])

def update(t):
    global psi
    psi = spsolve(bck, fwd.dot(psi))
    line_psi_mag.set_ydata(normalize(mag(psi)))
    line_psi.set_ydata(np.real(psi))
    line_psi2.set_ydata(np.imag(psi))


ani = FuncAnimation(fig, update, 60, interval=100)
writer = PillowWriter(fps=10)  
ani.save("5_superposition.gif", writer=writer)  

plt.show()
