import random
import string

from web3 import Web3


def convert_to_eip55_address(address):
    return Web3.to_checksum_address(address)


def generate_public_address():
    hex_chars = string.hexdigits.lower()
    return '0x' + ''.join(random.choices(hex_chars, k=40))


def generate_eip55_address():
    public_address = generate_public_address()
    return convert_to_eip55_address(public_address)
