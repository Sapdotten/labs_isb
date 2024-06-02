import time
from PyQt5 import QtCore
from lab_4.tools.bank_card import BankCardIterator
import multiprocessing as mp
from lab_4.tools.card_hash import CardHash


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
        self.card = None
        self.hash = None
        self.calculated = False
        self.card_number = None

    def set_card_data(self, hash: str, card_type: str, bank: str, numbers: str):
        self.hash = CardHash(hash)
        self.card = BankCardIterator(card_type, bank, numbers)

    def run(self):
        cores = mp.cpu_count()
        with mp.Pool(processes=cores) as p:
            for result, card_num in p.map(self.hash.check, self.card):
                if result:
                    self.ended = True
                    self.calculated = True
                    self.card_number = card_num
                    p.terminate()

                    break
        self.ended = True
