#!/usr/bin/env python3
from functools import wraps


# Solution Three
def rgb(red, green, blue):
    return red, green, blue


class Color:
    red = rgb(255, 0, 0)
    green = rgb(0, 255, 0)
    blue = rgb(0, 0, 255)
# END


# Solution Four
CLASSES = {}


def add(clazz):
    key = '{module}{name}'.format(
        module=clazz.__module__,
        name=clazz.__name__,
    )
    CLASSES[key] = clazz
# END


# Solution Five
def rgb2tuple(rgb):
    if isinstance(rgb, RGB):
        return rgb.red, rgb.green, rgb.blue


class RGB:
    red = 0
    green = 0
    blue = 0


red = RGB()
red.red = 255

green = RGB()
green.green = 255

blue = RGB()
blue.blue = 255
# END


# Solution Six
class CounterOne:
    value = 0

    def increase(self, delta=1):
        self.value = max(self.value + delta, 0)

    def decrease(self, delta=1):
        self.increase(-delta)
# END


# Solution Seven
class CounterTwo:
    def __init__(self, value=0):
        self.value = value

    def increase(self, delta=1):
        return CounterTwo(max(self.value + delta, 0))

    def decrease(self, delta=1):
        return self.increase(-delta)
# END


# Solution Eight
class HourClock:
    def __init__(self):
        self.__position = 0

    @property
    def hours(self):
        return self.__position

    @hours.setter
    def hours(self, new_position):
        self.__position = new_position % 12
# END


# Solution Nine
class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


class LimitedCounter(Counter):
    """A ounter with limited maximal value."""

    def __init__(self, limit):
        """Initialize a new counter with some limit."""
        super().__init__()
        self.__limit = limit

    def inc(self, amount=1):
        super().inc(amount)
        self.value = min(self.value, self.__limit)


# OR
class LimitedCounter2(Counter):
    """A counter with limited maximal value."""

    def __init__(self, limit):
        """Initialize a new counter with some limit."""
        self.__limit = limit
        self.__actual_value = 0
        super().__init__()

    @property
    def value(self):
        return self.__actual_value

    @value.setter
    def value(self, new_value):
        self.__actual_value = min(new_value, self.__limit)
# END


# Solution Ten
def suppress(exception, *, or_return=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception:
                return or_return
        return inner
    return wrapper
# END


def main():
    pass


if __name__ == '__main__':
    main()
