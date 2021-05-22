import numpy as np
import scipy
from findiff import FinDiff
import matplotlib.pyplot as plt


nx = 1000
x = np.linspace(-1, 1, nx)
dx = x[1] - x[0]


d2_dx2 = FinDiff(0, dx, 2, acc=2)

V = np.full(x.shape, 1000.0)
V[50 : 950] = 0.0

_V = V[:]
V = scipy.sparse.diags(V)
H = - 0.5 * d2_dx2.matrix(x.shape) + V
spectrum, states = scipy.sparse.linalg.eigs(H, which='SR', k=5)

mag = lambda x: (x * np.conj(x)).real
normalize = lambda x: x / np.linalg.norm(x)

plt.subplot(211)
plt.plot(x, _V, color="black", linewidth=2)
plt.ylim(-0.1 , 1)
plt.ylabel('U(x)')

plt.grid()


plt.subplot(212)
for n, (energy, state) in enumerate(list(zip(spectrum, np.transpose(states)))[:3]):
    plt.plot(x, normalize(mag(state)), '-', label=f'n={n} E={energy.real:.1f}')

plt.ylabel('$\Psi^2(x)$')
plt.xlabel('x')
plt.grid()
plt.legend(loc='best')

plt.show()
