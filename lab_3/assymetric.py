import logging
from typing import Union

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


class AssymerticEncryption:
    """
    Class for assymtric encryption
    """
    private_key = None
    public_key = None
    public_key_path = None
    private_key_path = None

    def set_public_key_file_path(self, path: str):
        """
        Sets a path to file for public key
        :param path: path to file
        """
        self.public_key_path = path

    def set_private_key_file_path(self, path: str):
        """
        Set a path to file for private key
        :param path: path to file
        """
        self.private_key_path = path

    def generate_keys(self, length: int):
        """
        Generates keys for assymetric encrytpion
        :param length: length of key
        """
        try:
            keys = rsa.generate_private_key(
                public_exponent=65537,
                key_size=length
            )
            self.private_key = keys
            self.public_key = keys.public_key()
        except Exception as e:
            logging.error(f"Error in generating assymetric keys: {e}")

    @staticmethod
    def encrypt_data(key: bytes, data: bytes) -> Union[bytes, None]:
        """
        Encrypts a data using assymetric algorithm
        :param key: public key in bytes for assymetric encrytpion
        :param data: data for assymetric encryption
        :return: encoded data, None if error
        """
        try:
            key = load_pem_public_key(key)
        except Exception as e:
            logging.error(f"Unsuccesful try to decode public key bytes: {e}")
        else:
            try:
                return key.encrypt(data,
                                   padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                algorithm=hashes.SHA256(),
                                                label=None))
            except Exception as e:
                logging.error(f"Unsuccesful try to encode data using private key: {e}")
        return None

    @staticmethod
    def decrypt_data(key: bytes, data: bytes) -> Union[bytes, None]:
        """
        Decrypts a data using assymetric algorithm
        :param key: private key in bytes for decrypting
        :param data: encrypted data
        :return: decrypted data, None if error
        """
        try:
            key = load_pem_private_key(key, password=None, )
        except Exception as e:
            logging.error(f"Unsuccesful try to decode private key bytes: {e}")
        else:
            try:
                return key.decrypt(data,
                                   padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                                label=None))
            except Exception as e:
                logging.error(f"Unsuccesful try to decode data using private key: {e}")
        return None
