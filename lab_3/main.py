import argparse
import logging
from typing import Union

from hybrid_system import HybridSystem
from file_service import FileService
from args_parsing import config_argparse
import consts

if __name__ == '__main__':
    settings = FileService.read_json(consts.SETTINGS)
    args = config_argparse(settings)
    if args.generation:
        hybrid_system = HybridSystem(settings.get('symmetric_key', None),
                                     settings.get('public_key', None),
                                     settings.get('private_key', None))
        if args.symmetric_key_len is not None and args.asymmetric_key_len is not None:
            hybrid_system.generate_keys(args.symmetric_key_len, args.asymmetric_key_len)
        else:
            logging.error("There are no any args for lengths of keys. Add them using -sklen and -asklen")
    elif args.encryption:
        HybridSystem.encrypt_text(settings.get('initial_file', None),
                                  settings.get('private_key', None),
                                  settings.get('symmetric_key', None),
                                  settings.get('encrypted_file', None))
    # шифруем
    elif args.decryption:
        HybridSystem.decrypt_data(settings.get('encrypted_file', None),
                                  settings.get('private_key', None),
                                  settings.get('symmetric_key', None),
                                  settings.get('decrypted_file', None))
