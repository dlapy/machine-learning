from re import S
import numpy as np

class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):
        s = np.dot(self.w,x)
        return s

Xi = np.array([1, 0, 0, 1])
Wi = np.array([5, 4, 1, 1])
n = Neuron(Wi)
print('S= ', n.y(Xi))