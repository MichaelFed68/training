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
