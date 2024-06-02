import time
import multiprocessing as mp

from typing import Tuple

from tools.card_hash import CardHash


class Statistics:
    def __init__(self):
        super().__init__()
        self.cores = mp.cpu_count()
        self.x = []
        self.y = []

    def set_card_data(self, hash: str, card_type: str, bank: str, numbers: str):
        self.hash = hash
        self.card_type = card_type
        self.bank = bank
        self.numbers = numbers

    def calculate_stats(self) -> Tuple[list, list]:
        for i in range(1, int(self.cores * 1.5) + 1):
            hash_check = CardHash(self.hash, self.card_type, self.bank, self.numbers)
            time0 = time.time()
            hash_check.calculate_card_number(i)
            while not hash_check.calculated:
                pass
            time1 = time.time()
            self.x.append(i)
            self.y.append(time1 - time0)
        return self.x, self.y
