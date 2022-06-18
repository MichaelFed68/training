#!/usr/bin/env python3


# Solution Two
def greet(name, *args):
    names = " and ".join((name,) + args)
    string_name = 'Hello, {}!'.format(names)
    return string_name

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
def filter_map(func, iterable):
    res = []
    for predicate, value in map(func, iterable):
        if predicate:
            res.append(value)
    return res
# OR
def filter_map_another(func, iterable):
    return [pair[1] for pair in map(func, iterable) if pair[0]]
# END


# Solution Seven
from functools import reduce
from operator import getitem

def keep_truthful(iterable):
    return filter(None, iterable)

def abs_sum(iterable):
    return sum(map(abs, iterable))

def walk(dict, iterable_path):
    return reduce(getitem, iterable_path, dict)
# END


# Solution Eight
def partial_apply(func, arg1):
        def inner(arg2):
            return func(arg1, arg2)
        return inner
 
def flip(func):
    def inner(arg1, arg2):
        return func(arg2, arg1)
    return inner
# END


# Solution Nine
def make_module(step=1):
    return {
        'inc': lambda x: x + step,
        'dec': lambda x: x - step
    }    
# END


# Solution Ten
def memoized(func):
    memory = {}

    def make_mem(num):
        if num in memory:
            return memory[num]
        memory[num] = func(num)
        return memory[num]

    return make_mem
# END


# Solution Eleven
from functools import wraps


def memoizing(max_size):
    def wrapped(func):
        keys = []
        memory = {}
        @wraps(func)
        def inner(num):
            res = memory.get(num)
            if res is None:
                res = func(num)
                keys.append(num)
                if len(keys) > max_size:
                    del memory[keys.pop(0)]
                    memory[num] = res
            return res
        return inner
    return wrapped
# END


def main():
    @memoizing(3)
    def f(x):
        """Multiplying by 10"""
        print('Calculating..., x = {}'.format(x))
        return x * 10

    print(f(1))
    print(f(1))
    print(f(2))
    print(f(3))
    print(f.__closure__[1].cell_contents)
    print(f.__closure__[3].cell_contents)
    print(f(4))
    print(help(f))
    print(f.__closure__[1].cell_contents)
    print(f.__closure__[3].cell_contents)

if __name__ == '__main__':
    main()