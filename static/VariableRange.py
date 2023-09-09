from math import log, ceil
import matplotlib.pyplot as plt
from numpy import std, median, var


class VariableRange:
    def __init__(self, array):
        self.array = array
        self.n = len(array)
        self.r = max(array) - min(array)
        self.m = ceil(1 + 3.22 * log(self.n))
        self.dx = self.r / self.m
        self.cap_s = []
        self.lower_s = [0] * self.m

    def variable_matrix(self):
        for i in range(self.m + 1):
            self.cap_s.append(min(self.array) + self.dx * i)

        for i in self.array:
            for j in range(len(self.cap_s) - 1):
                if self.cap_s[j] <= i <= self.cap_s[j + 1]:
                    self.lower_s[j] += 1
        return [self.cap_s, self.lower_s]

    def graphic(self):
        self.variable_matrix()
        lower = list(map(float, self.lower_s))
        gr_arr = self.cap_s[:-1]
        for i in range(len(gr_arr) - 1):
            gr_arr[i] += self.dx / 2
        plt.title("Распределение выборки")
        plt.bar(gr_arr, lower)
        plt.show()

    def var(self):
        return var(self.array)

    def median(self):
        return median(self.array)

    def std(self):
        return std(self.array)
