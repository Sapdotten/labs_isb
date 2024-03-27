from typing import Union
from copy import copy
from constants import *


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


class RouteTransposition:
    def __init__(self, key: str, table_height: int):
        """
        :param key: key for encoding/decoding text
        :param table_height: height of coding table
        """
        self.key = self._process_key(key)
        self.height = table_height
        self.width = len(self.key)

    def _process_key(self, key: str) -> str:
        """
        Process the key by deleting excess symbols
        :param key: unprepared key
        :return: processed key only with letters for encoding text
        """
        return "".join(c for c in key if c.isalpha())

    def _prepare_text(self, src_text: str) -> str:
        """
        Preparing text for encoding by making it even encoding table size
        :param src_text: source not encoded text
        :return: text with suitable size
        """
        if (len(src_text) % (self.height * self.width)) == 0:
            return src_text
        text = copy(src_text)
        while (len(text) % (self.height * self.width)) != 0:
            text += " "
            text += src_text[:((self.width * self.height) - (len(text) % (self.height * self.width)))]
        return text

    def _get_reshuffle_order(self) -> list[int]:
        """
        Returns an order of reshuffle columns in encoding table
        :return: order of columns as list
        """
        sort_list = [i for i in range(0, len(self.key))]
        sort_list = sorted(sort_list, key=lambda k: self.key[k])
        return sort_list

    def _encode(self, text: str) -> str:
        """
        Encoding prepared text
        :param text: prepared text
        :return: encoding text
        """
        order = self._get_reshuffle_order()
        res = ""
        while len(text) > 0:
            table = []
            for i in range(0, self.width):
                if i % 2 == 0:
                    table.append(text[:self.height])
                else:
                    table.append(text[self.height - 1::-1])
                text = text[self.height:]
            for i in order:
                res += table[i]
        return res

    def encode(self, text: str) -> str:
        """
        Encoding text
        :param text: text for encoding
        :return: encoded text
        """
        text = self._prepare_text(text)
        return self._encode(text)

    def decode(self, text: str):
        """
        Decoding encoded text
        :param text: encoded text
        :return: decoded text
        """
        if len(text) % (self.width * self.height) != 0:
            raise RuntimeError("Encdoded text has invalid length")
        old_order = self._get_reshuffle_order()
        new_order = sorted(old_order, key=lambda k: old_order[k])
        res = ""
        while len(text) > 0:
            table = []
            for i in range(0, self.width):
                table.append(text[:self.height])
                text = text[self.height:]
            for i in new_order:
                if old_order[i] % 2 == 0:
                    res += table[i]
                else:
                    res += table[i][::-1]
        return res


def write_text_to_file(text: str, file_path: str) -> None:
    """
    Writes text to the file
    :param text: text
    :param file_path: path to file for write
    :return: None
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)


def encoding():
    text = read_text(SRC_TEXT_FILE)
    if text is None:
        print("Can't read the file")
        return None
    print("Src text: ")
    print(text)
    code = RouteTransposition(ENCODING_KEY, TABLE_HEIGHT)
    text = code.encode(text)
    write_text_to_file(text, POINT_TEXT_FILE)
    print("\nEncoded text: ")
    print(text)


def decoding():
    text = read_text(POINT_TEXT_FILE)
    if text is None:
        print("Can't read the file")
        return None
    code = RouteTransposition(ENCODING_KEY, TABLE_HEIGHT)
    try:
        text = code.decode(text)
    except RuntimeError as err:
        print(err)
    else:
        print('\nDecoded test after encoding: ')
        print(text)


if __name__ == '__main__':
    encoding()
    decoding()
