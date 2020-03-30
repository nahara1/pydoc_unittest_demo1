# Project: Brewing Automation System - Capstone Project
# Purpose Details: To provide a sample code of how to implement Threading in Python
# Course: IST 440W - 001
# Author: Nahara
# Date Developed: 3/28/2020
# Last Date Changed: 3/28/2020
# Rev 1


import threading
import time
import random


def get_random_number(lowest, highest):
    """
    function to obtain a random number within a certain range
    :param lowest: the lowest that can be randomly generated
    :param highest: the highest value that can be randomly generated
    :return: a random number
    """
    random_number = random.randrange(1, 10)
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
    int1 = 3
    int2 = 2
    number1 = random.randrange(1, 10)
    print("Random number #1 btw 1-10: ", number1)
    number2 = random.randrange(10, 20)
    print("Random number #2 btw 1-10: ", number2)

    start_time = time.time()

    # Threads
    t1 = threading.Thread(target=add, args=(number1, number2))
    t2 = threading.Thread(target=subtract, args=(number1, number2))
    t3 = threading.Thread(target=multiply, args=(number1, number2))
    t4 = threading.Thread(target=divide, args=(number1, number2))

    # start t1
    t1.start()
    # start t2
    t2.start()
    # start t3
    t3.start()
    # start t4
    t4.start()

    # wait here until thread 1 is finished
    t1.join()
    # wait here until thread 2 is finished
    t2.join()
    # wait here until thread 3 is finished
    t3.join()
    # wait here until thread 4 is finished
    t4.join()

    # print this message when all 4 threads are finished

    print("--- %s seconds ---" % (round(time.time() - start_time, 5)))

    print("Done!")