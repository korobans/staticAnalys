from math import log, ceil
import matplotlib.pyplot as plt
from numpy import std, median, var, round, mean, sqrt, transpose, array
import numpy as np
from scipy.stats import t, levene, ttest_ind, f_oneway, pearsonr, linregress
import pandas as pd
from sklearn.linear_model import LinearRegression


class VariableRange:
    def __init__(self, array):
        self.array = array
        self.array2 = []
        self.array3 = []
        self.array4 = []
        self.array5 = []
        self.array6 = []
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

        self.cap_s = list(map(lambda x: round(x, 3), self.cap_s))
        return [self.cap_s, self.lower_s]

    def correlation_map(self, array2):
        self.array2 = array2
        plt.title('Поле рассеивания')
        plt.scatter(self.array, self.array2)
        plt.show()

    def moda(self):
        self.variable_matrix()
        pop = self.lower_s.index(max(self.lower_s))
        return self.cap_s[pop] + self.dx / 2

    def graphic(self):
        self.variable_matrix()
        lower = list(map(float, self.lower_s))
        gr_arr = self.cap_s[:-1]
        for i in range(len(gr_arr) - 1):
            gr_arr[i] += self.dx / 2
        plt.title("Распределение выборки")
        plt.bar(gr_arr, lower)
        plt.show()

    def confidence_interval(self, confidence=0.95):
        meann = mean(self.array)
        std_err = std(self.array, ddof=1) / sqrt(self.n)
        margin = std_err * t.ppf((1 + confidence) / 2, self.n - 1)
        lower_bound = meann - margin
        upper_bound = meann + margin
        return [lower_bound, upper_bound]

    def avg_static_hypothesis(self, second_array, alpha=0.05):
        self.array2 = second_array
        equal_var = levene(self.array, self.array2).pvalue > alpha
        t_statistic, p_value = ttest_ind(self.array, self.array2, equal_var=equal_var)

        if p_value >= alpha:
            return True
        else:
            return False

    def dispersion_static_hypothesis(self, second_array, alpha=0.05):
        self.array2 = second_array
        f_statistic = 0
        p_value = 0
        f_statistic, p_value = f_oneway(self.array, self.array2)
        if p_value < alpha:
            return [False, f_statistic, p_value]
        else:
            return [True, f_statistic, p_value]

    def dispersion(self):
        return var(self.array)

    def median(self):
        return median(self.array)

    def avg_deviation(self):
        return std(self.array)

    def avg(self):
        return sum(self.array) / self.n

    def scope(self):
        return self.r

    def correlation_coef(self, arr2, arr3, arr4, arr5):
        self.array2 = arr2
        self.array3 = arr3
        self.array4 = arr4
        self.array5 = arr5
        data = pd.DataFrame(array([self.array, self.array2, self.array3, self.array4, self.array5]).transpose())
        return data.corr().values.tolist()

    def correlation(self, arr2, alpha):
        self.array2 = arr2
        p_value, cor = pearsonr(self.array, self.array2)
        if p_value < alpha:
            return cor
        else:
            return False

    def regression(self, arr2):
        self.array3 = self.array[:]
        self.array = np.array(self.array).reshape(-1, 1)
        self.array2 = np.array(arr2)
        model = LinearRegression()
        model.fit(self.array, self.array2)
        y_pred = model.predict(self.array)
        slope, intercept, r_value, p_value, std_err = linregress(self.array3, self.array2)
        print(slope, intercept, r_value, p_value, std_err)
        plt.scatter(self.array, self.array2, color='blue', label='Actual')
        plt.plot(self.array, y_pred, color='red', label='Predicted')
        plt.xlabel('X')
        plt.ylabel('y')
        plt.title('Однофакторная линейная регрессия')
        plt.legend()
        plt.show()
        if p_value < 0.05:
            return [slope, intercept, r_value, p_value, std_err]
        else:
            return False

    def oneway(self, arr2, arr3, arr4, arr5, arr6):
        self.array2 = arr2
        self.array3 = arr3
        self.array4 = arr4
        self.array5 = arr5
        self.array6 = arr6

        f_value, p_value = f_oneway(self.array, self.array2, self.array3, self.array4, self.array4, self.array5, self.array6)

        if p_value < 0.05:
            return f_value
        else:
            return False
