from typing import Union
import constants
from collections import Counter
from copy import copy


def read_text(file_path: str) -> Union[str, None]:
    """
    Reads text from file
    :param file_path: path to file with text
    :return: text from file or None, if can't read file
    """
    text = None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except FileNotFoundError:
        return None


def save_text_to_file(text: str, file_path: str) -> bool:
    """
    Saves a text to the file
    :param text: text to save
    :param file_path: path to file
    :return: True if text has been saved, False else
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True
    except FileNotFoundError:
        return False


def get_ordered_letters(frequenses: Union[dict[str, float], Counter]) -> list[str]:
    """
    Returns a list of letters sorted by their frequenses
    :param frequenses: dict of letters andtheir frequenses
    :return: list of sorted letters
    """
    letters = sorted(frequenses.keys(), key=lambda k: frequenses[k])
    return letters


class Decode:
    STANDART_ORDERED_LETTERS = get_ordered_letters(constants.STANDART_FREQUENSES)

    def __init__(self, text):
        """
        :param text: encoded text
        """
        self.src_text = text
        self.decode_dict = self.make_decode_dict(get_ordered_letters(Counter(text)))
        self.translated_text = text

    def make_decode_dict(self, ordered_letters) -> dict[str, str]:
        """
        Makes a dict where key is the symbol of source text and value is the true symbol for this one
        :param ordered_letters: list of letters of source text ordered by their frequenses
        :return: dict where key is encoded sumbol and value is decoded one
        """
        return dict(zip(ordered_letters, self.STANDART_ORDERED_LETTERS))

    def decode_text(self) -> str:
        """
        Decodes the source text using a dict for decoding
        :return: decoded text
        """
        text = copy(self.src_text)
        for key in self.decode_dict.keys():
            text = text.replace(key, self.decode_dict[key])
        self.translated_text = text
        return text

    def correct_decode_dict(self, src_phrase, correct_phrase) -> None:
        """
        Corrects a decode_dict by known phrases in text.
        :param src_phrase: a phrase in decoded dict that looks like correct phrase
        :param correct_phrase: phrase that should be instead of src_phrase
        :return: decoded text
        """
        if len(src_phrase) != len(correct_phrase):
            raise RuntimeError("The try to correct decode dict is invalid: lenghts of phrases are different.")
        ind = self.translated_text.find(src_phrase)
        src_letters = self.src_text[ind:ind + len(src_phrase)]
        for i in range(0, len(src_letters)):
            for key in self.decode_dict.keys():
                if self.decode_dict[key] == correct_phrase[i]:
                    self.decode_dict[key] = self.decode_dict[src_letters[i]]
            self.decode_dict[src_letters[i]] = correct_phrase[i]

    def get_decode_key(self) -> str:
        """
        Makes a string that describe the decoding of src text
        :return: describe of decode_dict as str
        """
        res = ""
        for key in self.decode_dict.keys():
            res += f"{key} = {self.decode_dict[key]}\n"
        return res


def task() -> None:
    """
    The solving of a task
    :return: None
    """
    text = read_text(constants.SRC_TEXT_FILE)
    if text is None:
        return None
    decode = Decode(text)
    print(decode.decode_text(), '\n')
    decode.correct_decode_dict('АДМИСИТНРАНИВСЗМИ', 'АДМИНИСТРАТИВНЫМИ')
    print(decode.decode_text(), '\n')
    decode.correct_decode_dict('ИНЙОРМАШИОННОЖ ЬЕКОЛАСНОСТИ', 'ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ')
    print(decode.decode_text(), '\n')
    decode.correct_decode_dict('С ПОКВЯЕНИЕМ РАСПРЕДЕЯЕННЫЧ СИСТЕМ ОБРАБОТЛИ ДАННЫЧ',
                               'С ПОЯВЛЕНИЕМ РАСПРЕДЕЛЕННЫХ СИСТЕМ ОБРАБОТКИ ДАННЫХ')
    print(decode.decode_text(), '\n')
    decode.correct_decode_dict('А ТАКЭЕ МЕРЫ ПОЗВОЛЯЧЮИЕ ОПРЕДЕЛЯТУ ГТО ТАКИЕ НАРЖШЕНИЯ БЕЗОПАСНОСТИ ИМЕЛИ МЕСТО',
                               'А ТАКЖЕ МЕРЫ ПОЗВОЛЯЮЩИЕ ОПРЕДЕЛЯТЬ ЧТО ТАКИЕ НАРУШЕНИЯ БЕЗОПАСНОСТИ ИМЕЛИ МЕСТО')
    print(decode.decode_text(), '\n')
    decode.correct_decode_dict('ШИРОКОЭО', 'ШИРОКОГО')
    print(decode.decode_text(), '\n')
    decode.correct_decode_dict('ЪТАП', 'ЭТАП')
    print(decode.decode_text(), '\n')
    dict_describe = decode.get_decode_key()
    if not save_text_to_file(decode.translated_text, constants.POINT_TEXT_FILE):
        print("Decoded text was not saved to the file.")
    if not save_text_to_file(dict_describe, constants.KEY_TEXT_FILE):
        print("Key was not saved to the file")


if __name__ == '__main__':
    task()
