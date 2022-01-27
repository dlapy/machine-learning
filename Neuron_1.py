from re import S
import numpy as np
class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):
        s = np.dot(self.w, x)
        return s

Xi = np.array([2,3])
Wi = np.array([1,1])
n = Neuron(Wi)
print('S1= ', n.y(Xi))
Xi = np.array([5,6])
print('S2= ', n.y(Xi))