import json
import logging

from typing import Union


class FileService:
    """
    Class for working with json files
    """
    @staticmethod
    def read_json(path: str) -> Union[dict, None]:
        '''
        Reads data from json file
        :param path: path to file
        :return: dict with data
        '''
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Error in try of reading json file: {e}")
            return None

    @staticmethod
    def write_json(data: dict, path: str):
        """
        Writes data to json file
        :param data: data in dict
        :param path: path to file
        """
        try:
            with open(path, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            logging.error(f"Error in try to write data to json: {e}")
