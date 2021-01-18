import numpy as np
from .functionbase import TestFunction


class Michalewicz(TestFunction):
    def test_function(self, xx, m=10):
        f = - sum([np.sin(x) * np.float_power(np.sin(i * np.float_power(x, 2) / np.pi), 2 * m)
                   for i, x in enumerate(xx, start=1)])
        return f
