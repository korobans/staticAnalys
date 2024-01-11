import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout, QTextEdit, QFileDialog
from VariableRange import VariableRange
import csv


class TaskWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.file = ''
        self.first_array = []
        self.second_array = []
        self.third_array = []
        self.fourth_array = []
        self.fifth_array = []
        self.sixth_array = []
        self.x = []
        self.y = []

        self.setWindowTitle("Статистические действия")

        self.task_label = QLabel("Выберите действие:")
        self.task_combo = QComboBox()
        self.task_combo.addItem("Посчитать дисперсию")
        self.task_combo.addItem("Посчитать моду")
        self.task_combo.addItem("Посчитать доверительный интервал")
        self.task_combo.addItem("Посчитать среднеквадратичное отклонение")
        self.task_combo.addItem("Посчитать среднее арифметическое")
        self.task_combo.addItem("Посчитать размах")
        self.task_combo.addItem("Посчитать медиану")
        self.task_combo.addItem("Построить график распределения")
        self.task_combo.addItem("Построить карту корелляции")
        self.task_combo.addItem("Проверить гипотизу о равенстве статистических средних значений")
        self.task_combo.addItem("Проверить гипотизу о равенстве дисперсий")
        self.task_combo.addItem("Посчитать корреляцию")
        self.task_combo.addItem("Проверить значимость кореляции двух выборок")
        self.task_combo.addItem("Посчитать однофакторную регрессию")
        self.task_combo.addItem("Провести однофакторный дисперсионный анализ")

        self.button = QPushButton("Ок")
        self.button.clicked.connect(self.show_task)

        self.task_text = QTextEdit()
        self.task_text.setReadOnly(True)

        self.file_button = QPushButton("Выберите файл")
        self.file_button.clicked.connect(self.open_file)

        layout = QVBoxLayout()

        layout.addWidget(self.file_button)
        layout.addWidget(self.task_label)
        layout.addWidget(self.task_combo)
        layout.addWidget(self.button)
        layout.addWidget(self.task_text)

        self.setLayout(layout)
        self.resize(600, 400)

    def show_task(self):
        self.csv_read()
        selected_task = self.task_combo.currentText()
        if self.first_array:
            if selected_task == "Посчитать дисперсию":
                self.task_text.setPlainText(f'Дисперсия первой выборки: {VariableRange(self.first_array).dispersion()}'
                                            f'\nДисперсия второй выборки: {VariableRange(self.second_array).dispersion()}\n'
                                            f'Дисперсия третьей выборки: {VariableRange(self.third_array).dispersion()}\n'
                                            f'Дисперсия четвертой выборки: {VariableRange(self.fourth_array).dispersion()}\n'
                                            f'Дисперсия пятой выборки: {VariableRange(self.fifth_array).dispersion()}')
            elif selected_task == "Посчитать моду":
                self.task_text.setPlainText(f'Мода первой выборки: {VariableRange(self.first_array).moda()}\n'
                                            f'Мода второй выборки: {VariableRange(self.second_array).moda()}\n'
                                            f'Мода третьей выборки: {VariableRange(self.third_array).moda()}\n'
                                            f'Мода четвертой выборки: {VariableRange(self.fourth_array).moda()}\n'
                                            f'Мода пятой выборки: {VariableRange(self.fifth_array).moda()}\n')
            elif selected_task == "Посчитать доверительный интервал":
                self.task_text.setPlainText(f'Интервал первой выборки: {VariableRange(self.first_array).confidence_interval()}\n'
                                            f'Интервал второй выборки: {VariableRange(self.second_array).confidence_interval()}\n'
                                            f'Интервал третьей выборки: {VariableRange(self.third_array).confidence_interval()}\n'
                                            f'Интервал четвертой выборки: {VariableRange(self.fourth_array).confidence_interval()}\n'
                                            f'Интервал пятой выборки: {VariableRange(self.fifth_array).confidence_interval()}\n')
            elif selected_task == "Посчитать среднеквадратичное отклонение":
                self.task_text.setPlainText(f'Среднеквадратичное отклонение первой выборки: {VariableRange(self.first_array).avg_deviation()}\n'
                                            f'Среднеквадратичное отклонение второй выборки: {VariableRange(self.second_array).avg_deviation()}\n'
                                            f'Среднеквадратичное отклонение третьей выборки: {VariableRange(self.third_array).avg_deviation()}\n'
                                            f'Среднеквадратичное отклонение четвертой выборки: {VariableRange(self.fourth_array).avg_deviation()}\n'
                                            f'Среднеквадратичное отклонение пятой выборки: {VariableRange(self.fifth_array).avg_deviation()}\n')
            elif selected_task == "Посчитать среднее арифметическое":
                self.task_text.setPlainText(f'Среднее арифметическое первой выборки: {VariableRange(self.first_array).avg()}\n'
                                            f'Среднее арифметическое второй выборки: {VariableRange(self.second_array).avg()}\n'
                                            f'Среднее арифметическое третьей выборки: {VariableRange(self.third_array).avg()}\n'
                                            f'Среднее арифметическое четвертой выборки: {VariableRange(self.fourth_array).avg()}\n'
                                            f'Среднее арифметическое пятой выборки: {VariableRange(self.fifth_array).avg()}\n')
            elif selected_task == "Посчитать размах":
                self.task_text.setPlainText(f'Размах первой выборки: {VariableRange(self.first_array).scope()}\nРазмах второй выборки: {VariableRange(self.second_array).scope()}')
            elif selected_task == "Посчитать медиану":
                self.task_text.setPlainText(f'Медиана первой выборки: {VariableRange(self.first_array).median()}\nМедиана второй выборки: {VariableRange(self.second_array).median()}')
            elif selected_task == "Построить график распределения":
                self.task_text.setPlainText(f'Графики построены в отдельном окне')
                VariableRange(self.first_array).graphic()
                VariableRange(self.second_array).graphic()
            elif selected_task == "Построить карту корелляции":
                self.task_text.setPlainText(f'Карта построена в отдельном окне')
                VariableRange(self.first_array).correlation_map(self.second_array)
            elif selected_task == "Проверить гипотизу о равенстве статистических средних значений":
                if VariableRange(self.first_array).avg_static_hypothesis(self.second_array):
                    self.task_text.setPlainText('Не можем опровергнуть гипотезу, что мат. ожидания равны')
                else:
                    self.task_text.setPlainText('Можем опровергнуть гипотезу, что мат. ожидания равны')
            elif selected_task == "Проверить гипотизу о равенстве дисперсий":
                if VariableRange(self.first_array).dispersion_static_hypothesis(self.second_array)[0]:
                    self.task_text.setPlainText(f'Дисперсия 1-ой выборки: {VariableRange(self.first_array).dispersion()}\nДисперсия 2-ой выборки: {VariableRange(self.second_array).dispersion()}\nЗначение F-статистики: {VariableRange(self.first_array).dispersion_static_hypothesis(self.second_array)[1]}\nP-значение: {VariableRange(self.first_array).dispersion_static_hypothesis(self.second_array)[2]}\nДисперсии статистически одинаковы')
                else:
                    self.task_text.setPlainText(f'Дисперсия 1-ой выборки: {VariableRange(self.first_array).dispersion()}\nДисперсия 2-ой выборки: {VariableRange(self.second_array).dispersion()}\nЗначение F-статистики: {VariableRange(self.first_array).dispersion_static_hypothesis(self.second_array)[1]}\nP-значение: {VariableRange(self.first_array).dispersion_static_hypothesis(self.second_array)[2]}\nДисперсии статистически различаются')
            elif selected_task == "Посчитать корреляцию":
                self.task_text.setPlainText('')
                self.task_text.insertPlainText(f"Корреляция выборок:\n")
                for i in VariableRange(self.first_array).correlation_coef(self.second_array, self.third_array, self.fourth_array, self.fifth_array):
                    for j in i:
                        self.task_text.insertPlainText(f'{round(j, 3)}    ')
                    self.task_text.insertPlainText('\n')
            elif selected_task == "Проверить значимость кореляции двух выборок":
                if VariableRange(self.first_array).correlation(self.second_array, 0.05):
                    self.task_text.setPlainText(f"Кореляция значима\n{VariableRange(self.first_array).correlation(self.second_array, 0.05)}")
                else:
                    self.task_text.setPlainText("Кореляция не значима")
            elif selected_task == "Посчитать однофакторную регрессию":
                if VariableRange(self.first_array).regression(self.second_array):
                    slope, intercept, r_value, p_value, std_err = VariableRange(self.first_array).regression(self.second_array)
                    self.task_text.setPlainText("Уравнение регрессии: y = {:.2f}x + {:.2f}\n".format(slope, intercept))
                    self.task_text.insertPlainText("Коэффициент корреляции: r = {:.2f}\n".format(r_value))
                    self.task_text.insertPlainText("p-значение: p = {:.4f}\n".format(p_value))
                    self.task_text.insertPlainText("Стандартная ошибка: {:.3f}\n".format(std_err))
                else:
                    self.task_text.setPlainText("Регрессия не значима")
            elif selected_task == "Провести однофакторный дисперсионный анализ":
                if VariableRange(self.first_array).oneway(self.second_array, self.third_array, self.fourth_array, self.first_array, self.sixth_array):
                    self.task_text.setPlainText(f"f-значение: {VariableRange(self.first_array).oneway(self.second_array, self.third_array, self.fourth_array, self.first_array, self.sixth_array)}")
                else:
                    self.task_text.setPlainText("Анализ не значим")

    def open_file(self):
        self.file, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")

    def csv_read(self):
        if self.file != '':
            with open(self.file, newline='') as csvfile:
                file = csv.reader(csvfile, delimiter=',', quotechar='|')

                for row in file:
                    self.first_array.append(float(row[0]))
                    self.second_array.append(float(row[1]))
                    try:
                        self.third_array.append(float(row[2]))
                        self.fourth_array.append(float(row[3]))
                        self.fifth_array.append(float(row[4]))
                        self.sixth_array.append(float(row[5]))
                    except Exception:
                        pass

        else:
            self.task_text.setPlainText("Файл не выбран")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TaskWindow()
    window.show()
    sys.exit(app.exec_())
