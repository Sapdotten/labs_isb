from PyQt5.QtWidgets import (
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QLineEdit
)
from tools.luhn_algorithm import Luhn


class TestLuhnAlgorithm(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(400)
        self.label = QLabel()
        self.label.setText("Введите последовательность цифр")

        self.sequence = QLineEdit()
        self.sequence.setReadOnly(False)

        self.result_label = QLabel()
        self.result_label.setText("Здесь отобразится результат")

        self.result_button = QPushButton()
        self.result_button.setText("Проверить последовательность алгоритмом Луна")

        self.menu_button = QPushButton()
        self.menu_button.setText("Вернуться в меню")

        self.main_layout_v = QVBoxLayout(self)
        self.main_layout_v.addWidget(self.label)
        self.main_layout_v.addWidget(self.sequence)
        self.main_layout_v.addWidget(self.result_label)
        self.main_layout_v.addWidget(self.result_button)
        self.main_layout_v.addWidget(self.menu_button)

    def check_luhn(self):
        if Luhn.check(self.sequence.text()):
            self.result_label.setText("Последовательность корректная")
        else:
            self.result_label.setText("Последовательность некорректная")
