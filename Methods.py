from random import randint
import re

def enter (message):
    num = int(input(message))
    return num

def сreate_list_random_num (length, min, max):
    random_list = []
    for item in range(length):
        random_list.append(randint(min, max))
    return random_list

def list_unrepeat_num (any_list):
    set_of_elem = set(any_list)
    unrepeat = []
    for i in set_of_elem:
        count = 0
        for item in any_list:
            if i == item:
                count += 1
        if count == 1:
            unrepeat.append(i)
    return unrepeat