#!/usr/bin/env python3


# Solution Two
from ctypes.wintypes import RGB


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

# END


# Solution Five

# END

def main():
    colors = get_colors()
    print(colors['green'])

if __name__ == '__main__':
    main()