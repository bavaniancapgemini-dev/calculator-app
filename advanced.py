import math


def power(a, b):
    return a ** b


def square_root(a):

    if a < 0:
        return "Invalid Number"

    return math.sqrt(a)


def modulus(a, b):
    return a % b