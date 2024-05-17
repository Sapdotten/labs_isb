import logging
import os
from typing import Union

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricEncryption:
    INIT_BLOCK_MODE_LEN = 16
    key = None
    key_path = None
    key_len = None

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
        try:
            self.key = os.urandom(length)
        except Exception as e:
            logging.error(f"Fail try to generate symmetric key: {e}")

    def get_key_bytes(self) -> bytes:
        """
        Returns symmetric key in bytes
        :return: key
        """
        return self.key

    @classmethod
    def encrypt_data(cls, key: bytes, data: bytes) -> Union[bytes, None]:
        """
        Encrypts a data using symmetric algorithm
        :param key: public key in bytes for symmetric encrytpion
        :param data: data for symmetric encryption
        :return: encoded data, None if error
        """
        try:
            padder = padding.ANSIX923(len(key)).padder()
            padded_data = padder.update(data) + padder.finalize()
        except Exception as e:
            logging.error(f"Error in padding data: {e}")
            return None
        try:
            iv = os.urandom(cls.INIT_BLOCK_MODE_LEN)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            return encryptor.update(padded_data) + encryptor.finalize()+iv
        except Exception as e:
            logging.error(f"Error in encrypting data by symmetric key: {e}")

    @staticmethod
    def decrypt_data(key: bytes, data: bytes) -> Union[bytes, None]:
        """
        Decrypts data that was encrypted by symmetric encryption
        :param key: symmetric key
        :param data: encrypted data
        :return: decrypted data
        """
        try:
            cipher = Cipher(algorithms.AES(key), modes.CBC(data[-16:]))
            decryptor = cipher.decryptor()
            d_data = decryptor.update(data[:-16]) + decryptor.finalize()

            unpadder = padding.ANSIX923(len(key)).unpadder()
            return unpadder.update(d_data) + unpadder.finalize()
        except Exception as e:
            logging.error(f"Error in process of symmetric decrypting data: {e}")
            return None

