import json


class FileService:
    @staticmethod
    def read_json(path: str) -> dict:
        with open(path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_json(data: dict, path: str):
        with open(path, 'w') as f:
            json.dump(data, f)
