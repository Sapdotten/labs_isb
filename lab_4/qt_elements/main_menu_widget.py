from PyQt5.QtWidgets import (
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setText("Лабораторная работа №4\nВариант 19\nСеменова А.П.\nгруппа 6211")
        self.label.setStyleSheet("font-size: 18px;")

        self.button_first_task = QPushButton()
        self.button_first_task.setText("Подобрать номер карты по хэшу")
        self.button_first_task.setMinimumHeight(50)

        self.button_second_task = QPushButton()
        self.button_second_task.setText("Проверить последовательность алгоритмом Луна")
        self.button_second_task.setMinimumHeight(50)

        self.main_layout_v = QVBoxLayout(self)
        self.main_layout_v.addWidget(self.label)
        self.main_layout_v.addStretch()
        self.main_layout_v.addWidget(self.button_first_task)
        self.main_layout_v.addWidget(self.button_second_task)
