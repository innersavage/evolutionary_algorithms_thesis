import numpy as np
from .functionbase import TestFunction


class Wolfe(TestFunction):
    def test_function(self, xx):
        if len(xx) != 3:
            raise Exception
        f = 4 / 3 * np.float_power(np.float_power(xx[0], 2) + np.float_power(xx[1], 2) - xx[0] * xx[1], 0.75) + xx[2]
        return f
