import numpy as np
import scipy
from findiff import FinDiff
import matplotlib.pyplot as plt


nx = 1000
x = np.linspace(-1, 1, nx)
dx = x[1] - x[0]


d2_dx2 = FinDiff(0, dx, 2, acc=2)

V = np.full(x.shape, 1e9)
V[50 : 950] = 0.0

_V = V[:]
V = scipy.sparse.diags(V)
H = - 0.5 * d2_dx2.matrix(x.shape) + V
spectrum, states = scipy.sparse.linalg.eigs(H, which='SR', k=5)

mag = lambda x: (x * np.conj(x)).real
normalize = lambda x: x / np.linalg.norm(x)


fig, axes = plt.subplots(5)

for n, (energy, state, ax1) in enumerate(list(zip(spectrum, np.transpose(states), axes))):
    ax2 = ax1.twinx()

    ax1.set_title(f'n={n+1} E={np.real(energy):.2f}')
    ax1.plot(x, normalize(mag(state)), '-', color='crimson')
    ax1.set_ylabel('$\Psi^2(x)$', color='crimson')
    ax1.get_xaxis().set_visible(False)
    ax1.tick_params(left=False, labelleft=False)

    
    ax2.plot(x, _V, color="black", linewidth=2, label='U(x)')
    ax2.set_ylabel('U(x)')
    ax2.tick_params(right=False, labelright=False)


plt.show()
