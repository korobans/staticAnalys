import VariableRange as vr
import csv

s = []
with open('Выборка.csv', newline='') as csvfile:
    file = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in file:
        s.append(float(row[0][1:-1].replace(',', '.')))

vr.VariableRange(s).graphic()
