from random import randint
import re

def enter (message):
    num = int(input(message))
    return num

def сreate_list_random_num (length, min, max):
    random_list = []
    for item in range(length):
        random_list.append(randint(min, max + 1))
    return random_list

def list_unrepeat_num (any_list):
    any_list = list(set(any_list))
    return any_list