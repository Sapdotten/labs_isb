import logging
from typing import Union


class FileService:
    """
    A class for working with files, reading data from them and writing
    """

    @staticmethod
    def read_txt(path: str) -> Union[None, str]:
        """
        Read .txt files
        :param path: path to file
        :return: text from file, None if error
        """
        try:
            with open(path, 'r') as file:
                text = file.read()
            return text
        except FileNotFoundError:
            logging.error(f"File for reading wasn't found")
        except Exception as e:
            logging.error(f"Error in try of reading file: {e}")
        return None

    @staticmethod
    def write_txt(path: str, data: str):
        """
        Writes data to .txt file
        :param path: path to file
        :param data: data
        """
        try:
            with open(path, 'w') as file:
                file.write(data)
        except Exception as e:
            logging.error(f"Error in try save data to file: {e}")

    @staticmethod
    def read_bytes(path: str) -> Union[bytes, None]:
        """
        Read byte files
        :param path: path to file
        :return: bytes from file, None if error
        """
        try:
            with open(path, 'rb') as file:
                text = file.read()
            return text
        except FileNotFoundError:
            logging.error(f"File for reading wasn't found")
        except Exception as e:
            logging.error(f"Error in try of reading file: {e}")
        return None

    @staticmethod
    def write_bytes(path: str, data: bytes):
        """
         Writes data to byte file
         :param path: path to file
         :param data: data
         """
        try:
            with open(path, 'wb') as file:
                file.write(data)
        except Exception as e:
            logging.error(f"Error in try save data to file: {e}")
