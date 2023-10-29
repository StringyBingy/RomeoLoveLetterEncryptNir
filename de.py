"""
Author: Uri Geltner
Date: 22/9/2023
Description: this program decrypts and encrypts love letters according to a table of letters that correspond to numbers
and saves the encrypted message in a file that you can later decrypt from and print on a screen
"""
import sys
import os
import logging

LOG_FORMAT = '%(levelname)s | %(asctime)s | %(processName)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/logger.log'
FILE_PATH = r"C:\Users\myrtl\PycharmProjects\romeo\encrypted_msg.txt"
ENCRYPTION_TABLE = {
    'A': '56',
    'B': '57',
    'C': '58',
    'D': '59',
    'E': '40',
    'F': '41',
    'G': '42',
    'H': '43',
    'I': '44',
    'J': '45',
    'K': '46',
    'L': '47',
    'M': '48',
    'N': '49',
    'O': '60',
    'P': '61',
    'Q': '62',
    'R': '63',
    'S': '64',
    'T': '65',
    'U': '66',
    'V': '67',
    'W': '68',
    'X': '69',
    'Y': '10',
    'Z': '11',
    'a': '12',
    'b': '13',
    'c': '14',
    'd': '15',
    'e': '16',
    'f': '17',
    'g': '18',
    'h': '19',
    'i': '30',
    'j': '31',
    'k': '32',
    'l': '33',
    'm': '34',
    'n': '35',
    'o': '36',
    'p': '37',
    'q': '38',
    'r': '39',
    's': '90',
    't': '91',
    'u': '92',
    'v': '93',
    'w': '94',
    'x': '95',
    'y': '96',
    'z': '97',
    ' ': '98',
    ',': '99',
    '.': '100',
    ';': '101',
    '‘': '102',
    '?': '103',
    '!': '104',
    ':': '105'
}
DECRYPTION_TABLE = {
    56: 'A',
    57: 'B',
    58: 'C',
    59: 'D',
    40: 'E',
    41: 'F',
    42: 'G',
    43: 'H',
    44: 'I',
    45: 'J',
    46: 'K',
    47: 'L',
    48: 'M',
    49: 'N',
    60: 'O',
    61: 'P',
    62: 'Q',
    63: 'R',
    64: 'S',
    65: 'T',
    66: 'U',
    67: 'V',
    68: 'W',
    69: 'X',
    10: 'Y',
    11: 'Z',
    12: 'a',
    13: 'b',
    14: 'c',
    15: 'd',
    16: 'e',
    17: 'f',
    18: 'g',
    19: 'h',
    30: 'i',
    31: 'j',
    32: 'k',
    33: 'l',
    34: 'm',
    35: 'n',
    36: 'o',
    37: 'p',
    38: 'q',
    39: 'r',
    90: 's',
    91: 't',
    92: 'u',
    93: 'v',
    94: 'w',
    95: 'x',
    96: 'y',
    97: 'z',
    98: ' ',
    99: ',',
    100: '.',
    101: ';',
    102: '‘',
    103: '?',
    104: '!',
    105: ':'
}


def write_to_file(file_path, encrypted_msg):
    '''
    writes to file the encrypted message, then closes it
    :param: encrypted_msg
    :param: file_path
    :type encrypted_msg: string
    :type file_path: string
    :return: none
    '''
    try:
        with open(file_path, "w") as text_file:
            text_file.write(encrypted_msg)
            logging.debug(f"writing to file at: {file_path} was successful")
    except OSError:
        print("error opening file")
        logging.error("error while opening")


def read_from_file(file_path):
    '''
    reads the file and closes it
    :return: returns what is written in the file
    :rtype: string
    '''
    try:
        with open(file_path, "r") as file:
            text = file.read()
            logging.debug(f"file at: {file_path} was read successfully")
            return text
    except OSError:
        print("error while trying to read file")
        logging.error(f"error while trying to read file at {file_path}")
    return None


def encrypt(user_msg):
    '''
    encrypted the decrypted message from the text file
    :param: user_msg
    :type: string
    :return: string of decrypted message with commas inbetween the numbers
    :rtype: string
    '''
    msg = [char for char in user_msg]
    return ','.join(msg)


def decrypt():
    '''
    decrypt the encrypted message from the text file
    :return: the decrypted message
    :rtype: string
    '''
    decrypted_msg = read_from_file(FILE_PATH)
    msg_lst = [char for char in decrypted_msg.strip().split(',')]
    return ''.join(msg_lst)


def main():

    if sys.argv[1] == 'encrypt':
        user_msg = input('please enter a love letter please: ')
        encrypted_msg = encrypt(user_msg)
        write_to_file(FILE_PATH, encrypted_msg)

    elif sys.argv[1] == 'decrypt':
        print(decrypt())


if __name__ == '__main__':
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    if sys.argv[1] == 'decrypt':
        assert not read_from_file(FILE_PATH) == '', 'file empty'
    main()

