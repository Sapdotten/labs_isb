import json
import logging
from typing import Union


class FileService:
    """
    A class for working with files, reading data from them and writing
    """
    ENCODING = 'UTF-8'

    @classmethod
    def read_txt(cls, path: str) -> Union[None, str]:
        """
        Read .txt files
        :param path: path to file
        :return: text from file, None if error
        """
        try:
            with open(path, 'r', encoding=cls.ENCODING) as file:
                text = file.read()
            return text
        except FileNotFoundError:
            logging.error(f"File for reading wasn't found")
        except Exception as e:
            logging.error(f"Error in try of reading file: {e}")
        return None

    @classmethod
    def write_txt(cls, path: str, data: str):
        """
        Writes data to .txt file
        :param path: path to file
        :param data: data
        """
        try:
            with open(path, 'w', encoding=cls.ENCODING) as file:
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

    @staticmethod
    def read_json(path: str) -> Union[dict, None]:
        """
        Reads json file
        :param path: path to json file
        :return: dict with data or None, if error
        """
        try:
            with open(path, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            logging.error(f"Error in try to read json file: {e}")
            return None
