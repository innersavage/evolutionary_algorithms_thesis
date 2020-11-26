import numpy as np
from .functionbase import TestFunction


class Rastrigin(TestFunction):
    def test_function(self, xx, a=10):
        f = a * len(xx) + sum([np.power(x, 2) - a * np.cos(2 * np.pi * x) for x in xx])
        return f
