#!/usr/bin/env python3

from math import sqrt

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


def main():
    print(get_range(10))
    print(get_square_roots(49))
    
    list = ['nn', 'hh']
    duplicate(list)
    print(list)

if __name__ == '__main__':
    main()