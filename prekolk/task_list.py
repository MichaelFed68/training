#!/usr/bin/env python3

from math import sqrt
from os import lseek

# Solution for Lesson Three
def get_square_roots(num):

    if num < 0:
        return None
    elif num == 0:
        return [num]
    else:
        root = sqrt(num)
        return [-root, root]

def get_range(num):
    if num <= 0:
        return []
    else:
        res = []
        i = 0
        while i < num:
            res.append(i)
            i += 1
        return res

# Solution for Lesson Five
def duplicate(list):
    list = list.extend(list)

# Solution for lesson Six
def rotate(list):
    if list != []:
        list.insert(0, list.pop(-1))

# Solution for lesson Seven
def rotaded_left(obj):
    return obj[1:] + obj[:1]

def rotaded_right(obj):
    return obj[-1:]+ obj[:-1]

def main():
    print(get_range(10))
    print(get_square_roots(49))
    
    lst = [1, 3, 5]

    duplicate(lst)
    print(lst)

    rotate(lst)
    print(lst)

    print(rotaded_right(lst))
    print(rotaded_left(lst))

if __name__ == '__main__':
    main()