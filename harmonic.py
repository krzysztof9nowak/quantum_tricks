import numpy as np
import scipy
from findiff import FinDiff
import matplotlib.pyplot as plt


nx = 1000
x = np.linspace(-10, 10, nx)
dx = x[1] - x[0]


d2_dx2 = FinDiff(0, dx, 2, acc=2)
# V = 0.5 * x**2
# V = -1 / np.abs(x)

V = np.full(x.shape, 1000.0)
V[50 : 950] = 0.0
V[450 : 750] = 0.2

# V = np.full(x.shape, 0.0)

_V = V[:]
V = scipy.sparse.diags(V)
H = - 0.5 * d2_dx2.matrix(x.shape) + V
spectrum, states = scipy.sparse.linalg.eigs(H, which='SR', k=5)

mag = lambda x: (x * np.conj(x)).real

plt.subplot(211)
for energy, state in list(zip(spectrum, np.transpose(states)))[3:]:
    plt.plot(x, mag(state), '.-', label=f'E={energy.real:.3f}')

plt.ylabel('Ψ^2')
plt.grid()
plt.legend(loc='best')

plt.subplot(212)
plt.plot(x, _V)
plt.ylim(0,0.5)
plt.ylabel('U')
plt.xlabel('x')
plt.grid()

plt.show()
