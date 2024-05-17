import logging

from symmetric import SymmetricEncryption
from asymmetric import AsymerticEncryption
from file_service import FileService


class HybridSystem:
    """
    Class that realizes hybrid encoding
    """
    ENCODING = 'UTF-8'
    symmetric_key: bytes
    asymmetric_public_key: bytes
    asymmetric_private_key: bytes
    symmetric_file: str
    asymmetric_public_file: str
    asymmetric_private_file: str

    def __init__(self, symmetric_file: str, asymmetric_public_file: str, asymmetric_private_file: str):
        """
        :param symmetric_file: path to file for saving symmetric file
        :param asymmetric_public_file:  path to file for saving asymmetric public key
        :param asymmetric_private_file: path to file for saving asymmetric private key
        """
        self.symmetric_file = symmetric_file
        self.asymmetric_public_file = asymmetric_public_file
        self.asymmetric_private_file = asymmetric_private_file

    def generate_keys(self, symmetric_key_len: int, assymetric_key_len: int):
        """
        Generates keys
        :param symmetric_key_len: len of symmetric key
        :param assymetric_key_len: len of assymetric key
        """
        try:
            symmetric_key = SymmetricEncryption()
            symmetric_key.generate_key(symmetric_key_len)
        except ValueError:
            logging.error("Wrong value for length of symmetric key")
        self.symmetric_key = symmetric_key.get_key_bytes()
        asymmetric_key = AsymerticEncryption()
        asymmetric_key.generate_keys(assymetric_key_len)
        self.asymmetric_public_key = asymmetric_key.get_public_key_bytes()
        self.asymmetric_private_key = asymmetric_key.get_private_key_bytes()
        self.serialize_keys()

    def serialize_keys(self):
        """
        Serializes keys to files
        """
        FileService.write_bytes(self.asymmetric_public_file, self.asymmetric_public_key)
        FileService.write_bytes(self.asymmetric_private_file, self.asymmetric_private_key)
        FileService.write_bytes(self.symmetric_file,
                                AsymerticEncryption.encrypt_data(self.asymmetric_public_key, self.symmetric_key))

    @classmethod
    def encrypt_text(cls, text_file: str, private_key_file: str, symmetric_file: str, encoded_text_file: str):
        """
        Encrypts text using symmetric and asymmetric
        :param text_file: path to file with text
        :param private_key_file: path to file with private key
        :param symmetric_file: path to file with encoded symmetric key
        :param encoded_text_file: path to file for saving encoded text
        """
        asymmetric_private_key = FileService.read_bytes(private_key_file)
        symmetric_key = AsymerticEncryption.decrypt_data(asymmetric_private_key,
                                                         FileService.read_bytes(symmetric_file))
        text = FileService.read_txt(text_file)
        text = SymmetricEncryption.encrypt_data(symmetric_key, text)
        FileService.write_bytes(encoded_text_file, text)

    @classmethod
    def decrypt_data(cls, encoded_text_file: str, private_key_file: str, symmetric_file: str, decoded_text_file: str):
        """
        Decrypts text using symmetric and asymmetric
        :param encoded_text_file: path to file with encoded text
        :param private_key_file: path to file with private key
        :param symmetric_file: path to file with symmetric key
        :param decoded_text_file: path to file for saving decoded text
        :return:
        """
        asymmetric_private_key = FileService.read_bytes(private_key_file)
        symmetric_key = AsymerticEncryption.decrypt_data(asymmetric_private_key,
                                                         FileService.read_bytes(symmetric_file))
        text = FileService.read_bytes(encoded_text_file)
        text = SymmetricEncryption.decrypt_data(symmetric_key, text)
        FileService.write_txt(decoded_text_file, text)
