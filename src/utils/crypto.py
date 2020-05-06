import hmac
import hashlib
import binascii

from src.config import Config


class Crypto:
    @staticmethod
    def sha256(message):
        byte_key = binascii.unhexlify(Config.getConfig()['key']['hashSecret'])
        message = message.encode()
        return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()
