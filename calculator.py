# Project: pydoc and unittest demo
# Purpose Details: To provide a sample code of how to implement pydocs and unittest in Python
# Course: IST 440W - 001
# Author: Nahara
# Date Developed: 3/28/2020
# Last Date Changed: 3/28/2020
# Rev 1


import time
import random


def get_random_number(lowest, highest):
    """
    function to obtain a random number within a certain range
    :param lowest: the lowest that can be randomly generated
    :param highest: the highest value that can be randomly generated
    :return: a random number
    """
    random_number = random.randrange(lowest, highest)
    return random_number


def add(num1, num2):
    """
    function to add two numbers
    :param num1: a number
    :param num2: a number
    :return the addition of two numbers
    """
    return num1 + num2


def subtract(num1, num2):
    """
    function to subtract two numbers
    :param num1: a number
    :param num2: a number
    :return the difference of two numbers
    """
    return num1 - num2


def multiply(num1, num2):
    """
    function to multiply two numbers
    :param num1: a number
    :param num2: a number
    :return the product of two numbers
    """
    return num1 * num2


def divide(num1, num2):
    """
    function to divide two numbers
    :param num1
    :param num2
    :return the quotient of two numbers
    """
    return num1 / num2


if __name__ == "__main__":
    start_time = time.time()

    # get two random numbers
    int1 = get_random_number(10, 30)
    int2 = get_random_number(1, 10)

    print("random number #1: ", int1)
    print("random number #2: ", int2)
    print()

    # call operation methods
    print("Addition Result: ", add(int1, int2))
    print("Subtraction Result: ", subtract(int1, int2))
    print("Multiplication Result: ", multiply(int1, int2))
    print("Division Result: ", round(divide(int1, int2)), 3)

    # time taken to execute main
    print("--- %s seconds ---" % (round(time.time() - start_time, 5)))
