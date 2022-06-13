#!/usr/bin/env python3


# Solution Two
from ctypes.wintypes import RGB
from unittest import result


def greet(name, *args):
    names = " and ".join((name,) + args)
    return 'Hello, {}!'.format(names)

# END


# Solution Three
def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)

def get_colors():

    return dict(
        red=rgb(red=255),
        green=rgb(green=255),
        blue=rgb(blue=255)
        )
# END


# Solution Four
def updated(dictionary, **kwargs):
    copy_dictionary = dictionary.copy()
    copy_dictionary.update(kwargs)
    return copy_dictionary
# END


# Solution Five
def call_twice(function, *args, **kwargs):
    first = function(*args, **kwargs)
    second = function(*args, **kwargs)
    return first, second
# END


# Solution Six
def filter_map(function, iterable):
    res = []
    for predicate, value in map(function, iterable):
        if predicate:
            res.append(value)
    return res
# OR
def filter_map_another(function, iterable):
    return [pair[1] for pair in map(function, iterable) if pair[0]]
# END


def main():
    e = 1

if __name__ == '__main__':
    main()