"""
vigenere.py

This module provides functions for transforming text using a Vigenere cipher.

Ben Davies
2018 07 28
"""

CHARS = [c for c in (chr(i) for i in range(32, 127))]


def transform(text, key, want_decrypted=False):
    """Transform the supplied text and return the result.

    Args:
        text (str): The text to transform.
        key (str): The key with which to apply the transformation.
        want_decrypted (bool): Whether to encrypt (False) or decrypt (True).
    """
    res = ""
    for i, c in enumerate(text):
        if c not in CHARS:
            res += c
        else:
            text_index = CHARS.index(c)
            key_index = CHARS.index(key[i % len(key)])
            if want_decrypted:
                key_index *= -1
            res += CHARS[(text_index + key_index) % len(CHARS)]
    return res


def encrypt(text, key):
    """Encrypt the supplied text and return the result.

    Args:
        text (str): The text to encrypt.
        key (str): The key with which to perform the encryption.
    """
    return transform(text, key)


def decrypt(text, key):
    """Decrypt the supplied text and return the result.

    Args:
        text (str): The text to decrypt.
        key (str): The key with which to perform the decryption.
    """
    return transform(text, key, True)
