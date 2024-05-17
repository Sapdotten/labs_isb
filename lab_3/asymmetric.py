import logging
from typing import Union

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives import serialization


class AsymerticEncryption:
    """
    Class for asymmetric encryption
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
        Generates keys for asymmetric encrytpion
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
            logging.error(f"Error in generating asymmetric keys: {e}")

    def get_private_key_bytes(self) -> Union[bytes, None]:
        """
        Returns bytes of private key
        :return: bytes, None if error
        """
        try:
            return self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                  encryption_algorithm=serialization.NoEncryption())
        except Exception as e:
            logging.error(f"Error in try to get bytes of private key: {e}")
            return None

    def get_public_key_bytes(self) -> Union[bytes, None]:
        """
        Returns bytes of public key
        :return: bytes, None if error
        """
        try:
            return self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PublicFormat.SubjectPublicKeyInfo)
        except Exception as e:
            logging.error(f"Error in try to get bytes of public key: {e}")
            return None

    @staticmethod
    def encrypt_data(key: bytes, data: bytes) -> Union[bytes, None]:
        """
        Encrypts a data using asymmetric algorithm
        :param key: public key in bytes for asymmetric encrytpion
        :param data: data for asymmetric encryption
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
        Decrypts a data using asymmetric algorithm
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
