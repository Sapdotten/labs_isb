import logging

from tools.file_service import FileService
from tools.consts import BINS_FILE


class BankCardIterator:
    """
    Class for iteration by cards of sonme bank and card type
    """
    BINS_FILE = BINS_FILE
    FREE_PART_LEN = 6

    def __init__(self, card_type: str, bank: str, last_numbers: str):
        bins = FileService.read_json(self.BINS_FILE)
        try:
            self.bins = bins[card_type][bank]
        except KeyError:
            logging.error("Uncorrect type of card or bank")

        self.current_bin_num = 0
        self.current_free_sequence = '0' * self.FREE_PART_LEN
        self.last_numbers = last_numbers

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.current_bin_num == len(self.bins):
            raise StopIteration
        result = self.bins[self.current_bin_num] + self.current_free_sequence+self.last_numbers
        next_sequence = str(int(self.current_free_sequence) + 1)
        zeros_count = self.FREE_PART_LEN - len(next_sequence)
        if zeros_count < 0:
            self.current_free_sequence = '0' * self.FREE_PART_LEN
            self.current_bin_num += 1
        else:
            self.current_free_sequence = '0' * zeros_count + next_sequence
        return result
