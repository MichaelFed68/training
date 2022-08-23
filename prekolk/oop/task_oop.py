#!/usr/bin/env python3


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


# Solution Three
# END

# Solution Three
# END

# Solution Three
# END

# Solution Three
# END

# Solution Three
# END

def main():
    pass


if __name__ == '__main__':
    main()
