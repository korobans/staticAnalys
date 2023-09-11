from VariableRange import VariableRange
import csv


def csv_read(link, n=1):
    s = []
    n -= 1
    with open(link, newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in file:
            s.append(float(row[n]))
        return s


arr = csv_read('Выборки.csv', 1)
s = VariableRange(arr).variable_matrix()
for i in range(len(s[0]) - 1):
    print(f'{s[0][i]} - {s[0][i + 1]} --> {s[1][i]}')
print(VariableRange(arr).dispersion())
print(VariableRange(arr).avg_deviation())
print(VariableRange(arr).median())
print(VariableRange(arr).moda())
print(VariableRange(arr).avg())
print(VariableRange(arr).scope())
VariableRange(arr).graphic()
