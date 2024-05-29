import logging
import os
from typing import Union

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import (
    Cipher,
    algorithms,
    modes,
)


class SymmetricEncryption:
    INIT_BLOCK_MODE_LEN = 16
    ENCODING = 'UTF-8'
    key = None
    key_path = None

    def set_key_path(self, path: str):
        """
        Sets a path to file for key
        :param path: path to file
        """
        self.key_path = path

    def generate_key(self, length: int):
        """
        Generates a symmetric key
        :param length: lenght of key
        """
        if length not in [128, 192, 256]:
            raise ValueError("Incorrect value of length: it must be 128, 192 or 256")
        self.key = os.urandom(length // 8)

    def get_key_bytes(self) -> bytes:
        """
        Returns symmetric key in bytes
        :return: key
        """
        return self.key

    @classmethod
    def encrypt_data(cls, key: bytes, data: str) -> Union[bytes, None]:
        """
        Encrypts a data using symmetric algorithm
        :param key: public key in bytes for symmetric encrytpion
        :param data: data for symmetric encryption
        :return: encoded data, None if error
        """
        try:
            data = bytes(data, cls.ENCODING)
            padder = padding.ANSIX923(len(key) * 8).padder()
            padded_data = padder.update(data) + padder.finalize()
        except Exception as e:
            logging.error(f"Error in padding data: {e}")
            return None
        try:
            iv = os.urandom(cls.INIT_BLOCK_MODE_LEN)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            return encryptor.update(padded_data) + encryptor.finalize() + iv
        except Exception as e:
            logging.error(f"Error in encrypting data by symmetric key: {e}")

    @classmethod
    def decrypt_data(cls, key: bytes, data: bytes) -> Union[str, None]:
        """
        Decrypts data that was encrypted by symmetric encryption
        :param key: symmetric key
        :param data: encrypted data
        :return: decrypted data
        """
        try:
            cipher = Cipher(algorithms.AES(key), modes.CBC(data[-cls.INIT_BLOCK_MODE_LEN:]))
            decryptor = cipher.decryptor()
            d_data = decryptor.update(data[:-cls.INIT_BLOCK_MODE_LEN]) + decryptor.finalize()

            unpadder = padding.ANSIX923(len(key) * 8).unpadder()
            return (unpadder.update(d_data) + unpadder.finalize()).decode(cls.ENCODING)
        except Exception as e:
            logging.error(f"Error in process of symmetric decrypting data: {e}")
            return None
