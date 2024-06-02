import hashlib


class CardHash:
    def __init__(self, hash: str):
        self.hash = hash

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

