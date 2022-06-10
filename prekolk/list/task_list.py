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
# END


# Solution for Lesson Five
def duplicate(list):
    list = list.extend(list)
# END


# Solution for lesson Six
def rotate(list):
    if list != []:
        list.insert(0, list.pop(-1))
# END


# Solution for lesson Seven
def rotaded_left(obj):
    return obj[1:] + obj[:1]

def rotaded_right(obj):
    return obj[-1:]+ obj[:-1]
# END


# Solution for lesson Eight
def find_index(value, list):
    for (index, item) in enumerate(list):
        if item == value:
            return index 
    else:
        return None
# END


# Solution for lesson Nine
def find_second_index1(value, list):
    iterator = iter(list)
    first_index = find_index(value, iterator)
    
    if first_index != None:
        second_index = find_index(value, iterator)
        if second_index != None:
            return first_index + second_index + 1
    return None
#END


def main():
    lis = [2929, 'FFF,', 19, 10]
    print(find_second_index1(19, lis))

if __name__ == '__main__':
    main()