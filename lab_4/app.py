import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)

from qt_elements.main_menu_widget import MenuWidget
from qt_elements.first_task_widget import GetCardNumberWidget
from qt_elements.second_task_widget import TestLuhnAlgorithm
from qt_elements.third_task_widget import MatplotlibWidget
from tools.file_service import FileService
from tools.consts import BINS_FILE, CARD_NUMBER_FILE
from qt_elements.workers import (
    SlowTask,
    CalculateCardNumber,
    CalculateStatistics
)


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = None
        self.first_task_widget = None
        self.second_task_widget = None
        self.third_task_widget = None

        self.go_to_menu()

    def init_menu_widget(self):
        self.menu = MenuWidget()
        self.menu.button_first_task.clicked.connect(self.go_to_fisrt_task)
        self.menu.button_second_task.clicked.connect(self.go_to_second_task)

    def init_first_task_widget(self):

        self.first_task_widget = GetCardNumberWidget()
        self.first_task_widget.menu_button.clicked.connect(self.go_to_menu)

        bins = FileService.read_json(BINS_FILE)
        card_types = bins.keys()
        self.first_task_widget.type_card_box.addItems(card_types)
        self.first_task_widget.type_card_box.currentIndexChanged.connect(
            lambda: self.first_task_widget.set_banks(bins[self.first_task_widget.type_card_box.currentText()]))

        self.first_task_widget.result_button.clicked.connect(self.calculate_card_number)
        self.first_task_widget.stats_button.clicked.connect(self.get_statistics)

    def init_second_task_widget(self):
        self.second_task_widget = TestLuhnAlgorithm()
        self.second_task_widget.menu_button.clicked.connect(self.go_to_menu)
        self.second_task_widget.result_button.clicked.connect(self.check_luhn)

    def init_third_task_widget(self):
        self.third_task_widget = MatplotlibWidget()
        self.third_task_widget.menu_button.clicked.connect(self.go_to_menu)

    def go_to_fisrt_task(self):
        self.init_first_task_widget()
        self.setCentralWidget(self.first_task_widget)
        self.show()

    def go_to_second_task(self):
        self.init_second_task_widget()
        self.setCentralWidget(self.second_task_widget)
        self.show()

    def go_to_third_task(self):
        self.init_third_task_widget()
        self.setCentralWidget(self.init_third_task_widget())
        self.show()

    def go_to_menu(self):
        self.init_menu_widget()
        self.setCentralWidget(self.menu)
        self.show()

    def on_update_calculate_number(self, data):
        self.first_task_widget.progressbar.setValue(data)
        if self.process_card_num.ended:
            self.task.stop()
            self.first_task_widget.progressbar.hide()
            self.first_task_widget.set_result(self.process_card_num.card_number)
            if self.process_card_num.calculated:
                FileService.write_json({"card_number": self.process_card_num.card_number}, CARD_NUMBER_FILE)
                self.first_task_widget.set_file(CARD_NUMBER_FILE)
                QMessageBox.information(self, "Успех", "Мы смогли подобрать номер карты!")
            else:
                QMessageBox.critical(self, "Неудача", "Не удалось подобрать номер карты(")

    def check_card_data(self) -> bool:
        if len(self.first_task_widget.hash.text()) == 0:
            QMessageBox.critical(self, "Ошибка", "Введите значение хэша!")
        elif len(self.first_task_widget.numbers.text()) != 4:
            QMessageBox.critical(self, "Ошибка", "Что-то не так с количеством последних цифр...")
        elif not self.first_task_widget.numbers.text().isdecimal():
            QMessageBox.critical(self, "Ошибка", "Вместо последних четырех цифр вы ввели что-то другое")
        elif self.first_task_widget.type_card_box.currentText() == "Выберите тип карты":
            QMessageBox.critical(self, "Ошибка", "Вы не ввели тип карты!")
        elif self.first_task_widget.bank_box.currentText() == "Выберите банк карты":
            QMessageBox.critical(self, "Ошибка", "Вы не ввели банк карты!")
        else:
            return True
        return False

    def calculate_card_number(self):
        if not self.check_card_data():
            return None
        self.task = SlowTask(self)

        self.task.updated.connect(self.on_update_calculate_number)
        self.process_card_num = CalculateCardNumber()
        self.process_card_num.set_card_data(self.first_task_widget.hash.text(),
                                            self.first_task_widget.type_card_box.currentText(),
                                            self.first_task_widget.bank_box.currentText(),
                                            self.first_task_widget.numbers.text())
        self.first_task_widget.progressbar.show()
        self.task.start()
        self.process_card_num.start()

    def on_update_statistics(self, data):
        self.first_task_widget.progressbar.setValue(data)
        if self.calculate_statistics.ended:
            self.task.stop()
            self.first_task_widget.progressbar.hide()
            self.first_task_widget.plot.show()
            self.first_task_widget.plot.show_plot(self.calculate_statistics.x, self.calculate_statistics.y)

    def get_statistics(self):
        if not self.check_card_data():
            return None
        self.task = SlowTask(self)
        self.task.updated.connect(self.on_update_statistics)
        self.calculate_statistics = CalculateStatistics()

        self.calculate_statistics.set_card_data(self.first_task_widget.hash.text(),
                                                self.first_task_widget.type_card_box.currentText(),
                                                self.first_task_widget.bank_box.currentText(),
                                                self.first_task_widget.numbers.text())
        self.first_task_widget.progressbar.show()
        self.task.start()
        self.calculate_statistics.start()

    def check_luhn(self):
        if len(self.second_task_widget.sequence.text()) <= 1:
            QMessageBox.critical(self, "Ошибка", "Последовательность должна содержать не менее 2х цифр")
        elif not self.second_task_widget.sequence.text().isdecimal():
            QMessageBox.critical(self, "Ошибка", "Последовательность должна состоять из цифр")
        else:
            self.second_task_widget.check_luhn()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
