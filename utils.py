"""Utility functions for unary and gamma integer compression"""
import math

def unary_encode(x):
    """Returns the unary value of integer x.
    The number cannot be 0 or negative.

    >>> unary_encode(2)
    '0b10'
    """
    if x < 1:
        raise ValueError("Please pass int value >= 1.")
    else:
        return '0b' + (x-1) * '1' + '0'

def unary_decode(x):
    """Returns the integer representation of an unary value x.
    The unary value must be provided in '0b[...]' format.

    >>> unary_decode('0b10')
    2"""
    if not x.startswith('0b'):
        raise ValueError("Binary not properly formated. Please pass in following format '0b[...]'")
    else:
        if (x[2:].find('0') != len(x[2:])-1):
            raise ValueError("No unary encoding found.")
        else:
            return len(x[2:])

def gamma_encode(x):
    """Returns the gamma value of integer x.
    The number cannot be 0 or negative.

    >>> gamma_encode(5)
    '0b11001'
    """
    if x < 1:
        raise ValueError("Please pass int value >= 1.")
    else:
        logX = int(math.log(float(x), 2))
        unaryPart = unary_encode(1 + logX)
        binaryPart = "{0:b}".format(int(x - math.pow(2, logX)))
        while len(binaryPart) < logX:
            binaryPart = '0' + binaryPart
        return unaryPart + binaryPart

def gamma_decode(x):
    """Returns the integer representation of an gamma value x.
    The gamma value must be provided in '0b[...]' format.

    >>> gamma_decode('0b101')
    3"""
    if not x.startswith('0b'):
        raise ValueError("Binary not properly formated. Please pass in following format '0b[...]'")
    else:
        if (x[2:].find('0') < 1):
            raise ValueError("No gamma encoding found.")
        else:
            offset = x[2:].find('0') + 3
            unaryPart = unary_decode(x[:offset])
            binaryPart = int(x[offset:], 2)
            return math.pow(2, unaryPart - 1) + binaryPart