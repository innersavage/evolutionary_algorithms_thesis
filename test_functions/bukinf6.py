import numpy as np
from .functionbase import TestFunction


class BukinF6(TestFunction):
    def test_function(self, xx, a=10):
        if len(xx) != 2:
            raise Exception
        f = 100 * np.sqrt(np.fabs(xx[1] - 0.01 * np.power(xx[0], 2))) + 0.01 * np.fabs(xx[0] + 10)
        return f
