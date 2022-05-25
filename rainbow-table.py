import hashlib
import base64

CHAIN_LENGTH = 3

a = 'this is a string'


def generate_chain(hash_function, reduction_function, password: str) -> tuple:
    plaintext = password.encode('utf-8')
    chain = []
    for i in range(0, CHAIN_LENGTH):
        plaintext = hash_function(plaintext).hexdigest()
        chain.append(plaintext)
        plaintext = reduction_function(plaintext.encode('utf-8'))
    return tuple(password, chain[-1])


