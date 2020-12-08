import numpy as np
from .functionbase import TestFunction


class Rastrigin(TestFunction):
    def test_function(self, xx, a=10):
        f = sum([a - a * np.cos(2 * np.pi * x) + np.float_power(x, 2) for x in xx])
        return f
