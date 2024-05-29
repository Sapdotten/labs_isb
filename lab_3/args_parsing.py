import argparse


def config_argparse(settings: dict) -> argparse.Namespace:
    """
    Configs args for console
    :param settings: dict with default settings
    :return: args
    """
    parser = argparse.ArgumentParser()
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-gen', '--generation', action='store_true', help='Starts enerating of keys')
    mode_group.add_argument('-enc', '--encryption', action='store_true', help='Starts encoding mode')
    mode_group.add_argument('-dec', '--decryption', action='store_true', help='Starts decoding mode')

    settings_group = parser.add_argument_group()
    settings_group.add_argument('-sklen', '--symmetric_key_len',
                                type=int,
                                default=settings['symmetric_key_len'],
                                help="Len of symmetric key")
    settings_group.add_argument('-asklen', '--asymmetric_key_len',
                                type=int,
                                default=settings['asymmetric_key_len'],
                                help="Len of asymmetric key")
    settings_group.add_argument('-if', '--initial_file',
                                type=str,
                                default=settings['initial_file'],
                                help='File with text')
    settings_group.add_argument('-ef', '--encrypted_file',
                                type=str,
                                default=settings['encrypted_file'],
                                help='File with encrypted text')
    settings_group.add_argument('-df', '--decrypted_file',
                                type=str,
                                default=settings['decrypted_file'],
                                help='File with decrypted text')
    settings_group.add_argument('-sk', '--symmetric_key',
                                type=str,
                                default=settings['symmetric_key'],
                                help='File with symmetric key')
    settings_group.add_argument('-pbkey', '--public_key',
                                type=str,
                                default=settings['public_key'],
                                help='File with public key')
    settings_group.add_argument('-prkey', '--private_key',
                                type=str,
                                default=settings['private_key'],
                                help='File with private key')
    return parser.parse_args()
