import hashlib
import multiprocessing as mp

from lab_4.tools.bank_card import BankCardIterator


class CardHash:
    def __init__(self, hash: str, card_type: str, bank: str, numbers: str):
        self.hash = hash
        self.card = BankCardIterator(card_type, bank, numbers)
        self.card_number = None
        self.calculated = False

    def check(self, card_num: str) -> (bool, str):
        """
        Checks if card number can have hash like original
        :param card_num: number of card to check
        :return: true if card number is true
        """
        hashed = hashlib.sha3_256(card_num.encode()).hexdigest()
        if self.hash == hashed:
            return True, card_num
        return False, ''

    def calculate_card_number(self, cores: int = mp.cpu_count()):
        with mp.Pool(processes=cores) as p:
            for result, card_num in p.map(self.check, self.card):
                if result:
                    self.calculated = True
                    self.card_number = card_num
                    p.terminate()
                    break
