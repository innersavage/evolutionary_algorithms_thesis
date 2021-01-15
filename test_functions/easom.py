import numpy as np
from .functionbase import TestFunction


class Easom(TestFunction):
    def test_function(self, xx):
        if len(xx) != 2:
            raise Exception
        f = - np.cos(xx[0]) * np.cos(xx[1]) * np.exp(- np.float_power(xx[0] - np.pi, 2) - np.float_power(xx[1] - np.pi, 2))
        # f = - np.cos(xx[0]) * np.cos(xx[1]) * np.exp(-((xx[0]-np.pi)**2 - (xx[1]-np.pi)**2))
        return f
