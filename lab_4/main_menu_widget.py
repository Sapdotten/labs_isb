from PyQt5.QtWidgets import QPushButton, QApplication, QFileDialog, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, \
    QWidget, \
    QMessageBox

import sys


class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setText("Лабораторная работа №4, вар. 19, Семенова А.П., 6211")

        self.button_first_task = QPushButton()
        self.button_first_task.setText("Подобрать номер карты по хэшу")

        self.button_second_task = QPushButton()
        self.button_second_task.setText("Проверить последовательность алгоритмом Луна")

        self.button_third_task = QPushButton()
        self.button_third_task.setText("Исследовать время подбора для разного количества процессов")

        self.main_layout_v = QVBoxLayout(self)
        self.main_layout_v.addWidget(self.label)
        self.main_layout_v.addWidget(self.button_first_task)
        self.main_layout_v.addWidget(self.button_second_task)
        self.main_layout_v.addWidget(self.button_third_task)


