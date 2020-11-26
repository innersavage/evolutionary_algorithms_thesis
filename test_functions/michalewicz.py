import numpy as np
from .functionbase import TestFunction


class Michalewicz(TestFunction):
    def test_function(self, xx, m=10):
        f = - sum([np.sin(x) * np.power(np.sin(len(xx) * np.power(x, 2) / np.pi), 2 * m) for x in xx])
        return f
