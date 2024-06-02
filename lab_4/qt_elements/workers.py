import time

from PyQt5 import QtCore

from tools.card_hash import CardHash
from tools.statistics import Statistics


class SlowTask(QtCore.QThread):
    updated = QtCore.pyqtSignal(int)
    running = False

    def __init__(self, *args, **kwargs):
        super(SlowTask, self).__init__(*args, **kwargs)
        self.percent = 0
        self.running = True

    def run(self):
        while self.running:
            self.percent += 0.5
            self.percent %= 100
            self.updated.emit(int(self.percent))
            time.sleep(0.1)

    def stop(self):
        self.running = False


class CalculateCardNumber(QtCore.QThread):
    def __init__(self, *args, **kwargs):
        super(CalculateCardNumber, self).__init__(*args, **kwargs)
        self.ended = False
        self.hash = None
        self.calculated = False
        self.card_number = None

    def set_card_data(self, hash: str, card_type: str, bank: str, numbers: str):
        self.hash = CardHash(hash, card_type, bank, numbers)

    def run(self):
        self.hash.calculate_card_number()
        self.calculated = self.hash.calculated
        self.ended = True
        self.card_number = self.hash.card_number


class CalculateStatistics(QtCore.QThread):
    def __init__(self, *args, **kwargs):
        super(CalculateStatistics, self).__init__(*args, **kwargs)
        self.ended = False
        self.stats = Statistics()
        self.x = []
        self.y = []

    def set_card_data(self, hash: str, card_type: str, bank: str, numbers: str):
        self.stats.set_card_data(hash, card_type, bank, numbers)

    def run(self):
        self.x, self.y = self.stats.calculate_stats()
        self.ended = True
