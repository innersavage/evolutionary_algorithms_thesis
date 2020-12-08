import numpy as np


class TestFunction:
    def __init__(self, negative=False):
        self.negative = negative

    def calculate(self, xx, **kwargs):
        if len(xx) == 0:
            raise Exception
        xx = [x.astype(np.float128) for x in xx]
        result = self.test_function(xx, **kwargs)
        if self.negative:
            result = np.negative(result)
        return result

    def test_function(self, xx, **kwargs):
        raise NotImplementedError
