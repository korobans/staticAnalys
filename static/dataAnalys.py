# импортируем объект и библиотеку чтобы таблицу считать
from VariableRange import VariableRange
import csv


# ф-ия чтобы таблицу считать (в нее передаем название таблицы в папке локальной и номер столбца с выборкой)
def csv_read(link, n=1):
    s = []
    n -= 1
    # открываем табличку, на ньюлайн похуй, он у меня пустой вообще
    with open(link, newline='') as csvfile:
        # в файл считываем нашу таблицу через ридер (делиметр=разделитель, куотечар не помню, похуй на него, в таблице кстати замените все запятые на точки, а то ахуеете)
        file = csv.reader(csvfile, delimiter=',', quotechar='|')
        # записываем показания с таблицы в s
        for row in file:
            s.append(float(row[n]))
            # угадайте что строчка ниже делает
        return s


# смотрим что мы наделали, записываем выборку в переменную
arr = csv_read('Выборки.csv', 1)
# получаем таблицу вероятностей
s = VariableRange(arr).variable_matrix()
# красиво выводим ее
for i in range(len(s[0]) - 1):
    print(f'{s[0][i]} - {s[0][i + 1]} --> {s[1][i]}')
# ниже тест функций
print(VariableRange(arr).dispersion())
print(VariableRange(arr).avg_deviation())
print(VariableRange(arr).median())
print(VariableRange(arr).moda())
print(VariableRange(arr).avg())
print(VariableRange(arr).scope())
VariableRange(arr).graphic()
