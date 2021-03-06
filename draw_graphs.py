from test_functions import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator


def draw_graph(func, file=None, zlim=(-2.01, 2.01), rng=(-4.9, 5.10)):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    x = np.arange(rng[0], rng[1], 0.1)
    y = np.arange(rng[0], rng[1], 0.1)
    x, y = np.meshgrid(x, y)
    z = func([x, y])

    surf = ax.plot_surface(x, y, z, cmap=cm.plasma, linewidth=0, antialiased=False)

    ax.set_zlim(*zlim)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter('{x:.02f}')

    fig.colorbar(surf, shrink=0.5, aspect=5)

    if file is not None:
        plt.savefig('graphs/' + file)


graphs = [{'func': Rastrigin().calculate,
           'file': 'rastrigin.png',
           'zlim': (5, 90)},
          {'func': Easom().calculate,
           'file': 'easom.png',
           'zlim': (-1, 0.3),
           'rng': (-1, 7)},
          {'func': BukinF6().calculate,
           'file': 'bukin.png',
           'zlim': (-1, 300),
           'rng': (-14, 3)},
          {'func': Michalewicz().calculate,
           'file': 'michalewicz.png',
           'zlim': (-2, 0.5),
           'rng': (0, 4)}
          ]

for graph in graphs:
    draw_graph(**graph)
