from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, \
    QWidget, QComboBox, QLineEdit, QProgressBar


class GetCardNumberWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(400)
        self.label = QLabel()
        self.label.setText("Введите данные карты")

        self.hash_label = QLabel()
        self.hash_label.setText("Введите хэш карты")
        self.hash = QLineEdit()
        self.hash.setReadOnly(False)

        self.numbers_label = QLabel()
        self.numbers_label.setText("Введите последние 4 цифры карты")
        self.numbers = QLineEdit()
        self.numbers.setReadOnly(False)

        self.type_card_box = QComboBox()
        self.type_card_box.addItem("Выберите тип карты")

        self.bank_box = QComboBox()
        self.bank_box.addItem("Выберите банк карты")

        self.progressbar = QProgressBar(self)
        self.progressbar.hide()
        self.progressbar.setProperty("value", 0)

        self.result_label = QLabel()
        self.result_label.setText("Здесь отобразится результат")

        self.saved_to_label = QLabel()
        self.saved_to_label.setText("Номер карты сохранен в ...")

        self.result_button = QPushButton()
        self.result_button.setText("Подобрать номер карты")

        self.menu_button = QPushButton()
        self.menu_button.setText("Вернуться в меню")

        self.main_layout_v = QVBoxLayout(self)
        self.main_layout_v.addWidget(self.label)
        self.main_layout_v.addWidget(self.hash_label)
        self.main_layout_v.addWidget(self.hash)
        self.main_layout_v.addWidget(self.numbers_label)
        self.main_layout_v.addWidget(self.numbers)
        self.main_layout_v.addWidget(self.type_card_box)
        self.main_layout_v.addWidget(self.bank_box)
        self.main_layout_v.addWidget(self.progressbar)
        self.main_layout_v.addWidget(self.result_label)
        self.main_layout_v.addWidget(self.saved_to_label)
        self.main_layout_v.addWidget(self.result_button)
        self.main_layout_v.addWidget(self.menu_button)

    def set_banks(self, banks: list):
        self.bank_box.clear()
        self.bank_box.addItems(banks)

    def set_result(self, result: str):
        self.result_label.setText(f"Номер карты: {result}")

    def set_file(self, file_path: str):
        self.saved_to_label.setText(f"Номер карты сохранен в {file_path}")
