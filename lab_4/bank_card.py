import logging

from file_service import FileService
from consts import BINS_FILE


class BankCardIterator:
    """
    Class for iteration by cards of sonme bank and card type
    """
    BINS_FILE = BINS_FILE
    FREE_PART_LEN = 10

    def __init__(self, card_type: str, bank: str):
        bins = FileService.read_json(self.BINS_FILE)
        try:
            self.bins = bins[card_type][bank]
        except KeyError:
            logging.error("Uncorrect type of card or bank")

        self.current_bin_num = 0
        self.current_free_sequence = '0' * self.FREE_PART_LEN

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.current_bin_num == len(self.bins):
            raise StopIteration
        result = self.bins[self.current_bin_num] + self.current_free_sequence
        next_sequence = str(int(self.current_free_sequence) + 1)
        zeros_count = 10 - len(next_sequence)
        if zeros_count < 0:
            self.current_free_sequence = '0' * self.FREE_PART_LEN
            self.current_bin_num += 1
        else:
            self.current_free_sequence = '0' * zeros_count + next_sequence
        return result
