# импорт библиотек
from math import log, ceil
import matplotlib.pyplot as plt
from numpy import std, median, var, round


# объявление класса
class VariableRange:
    # стандартная функция с объявлением внутренних переменных, которые будут на весь класс распространяться
    def __init__(self, array):
        self.array = array
        self.n = len(array)
        self.r = max(array) - min(array)
        self.m = ceil(1 + 3.22 * log(self.n))
        self.dx = self.r / self.m
        self.cap_s = []
        self.lower_s = [0] * self.m

    # функция вывода таблицы
    def variable_matrix(self):
        # создание промежутков для таблицы
        for i in range(self.m + 1):
            self.cap_s.append(min(self.array) + self.dx * i)

        # подсчет кол-ва попаданий точки в промежуток
        for i in self.array:
            for j in range(len(self.cap_s) - 1):
                if self.cap_s[j] <= i <= self.cap_s[j + 1]:
                    self.lower_s[j] += 1
        # форматирование промежутков до 3 знаков после точки
        self.cap_s = list(map(lambda x: round(x, 3), self.cap_s))
        # ретурн епта
        return [self.cap_s, self.lower_s]

    # вызов функции с табличкой, чтобы моду найти
    def moda(self):
        self.variable_matrix()
        pop = self.lower_s.index(max(self.lower_s))
        return self.cap_s[pop] + self.dx / 2

    # функция для постройки графика
    def graphic(self):
        # вызов таблицы
        self.variable_matrix()
        # на всякий случай перевод кол-ва попаданий в числа с плавающей точкой
        lower = list(map(float, self.lower_s))
        # последнее число нам не нужно, поэтому его мы удаляем
        gr_arr = self.cap_s[:-1]
        # а к остальным прибавляем пол шага чтобы ровнее было (среднее отрезка)
        for i in range(len(gr_arr) - 1):
            gr_arr[i] += self.dx / 2
        # назваем график, распределяем оси и выводим график
        plt.title("Распределение выборки")
        plt.bar(gr_arr, lower)
        plt.show()

    # все функции что нужны для остального в umpy есть (мб и то, что выше есть, просто нахуй послали бы с такими завами)
    # дисперсия
    def dispersion(self):
        return var(self.array)

    # медиана
    def median(self):
        return median(self.array)

    # среднее отклонение
    def avg_deviation(self):
        return std(self.array)

    # среднее арифметическое
    def avg(self):
        return sum(self.array) / self.n

    # размах
    def scope(self):
        return self.r
