#!/usr/bin/env python3

# Solution for lesson Six
def toggle(flag, items):
    if flag in items:
        items.remove(flag)
    else:
        items.add(flag)


def toggled(flag, items):
    new_set = items.copy()

    if flag in items:
        new_set.remove(flag)
    else:
        new_set.add(flag)
    return new_set
# END

def main():
    l = [1, 2, 3]

if __name__ == '__main__':
    main()