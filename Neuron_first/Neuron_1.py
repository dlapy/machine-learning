# Модуль Neuron
import numpy as np

# Создание класса "Нейрон"
class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):             # Суммфтор
        s = np.dot(self.w, x)   # Суммируем входы
        return s                # Функция активации

Xi = np.array([2,3])    # Задаём значения входами
Wi = np.array([1,1])    # Веса входных сенсоров
n = Neuron(Wi)          # Создание объекта из класса Neuron
print('S1= ', n.y(Xi))  # Обращение к нейрону
Xi = np.array([5,6])    # Веса входных сенсоров
print('S2= ', n.y(Xi))  # Обращение к нейрону