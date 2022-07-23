#!/usr/bin/env python3

from itertools import chain


# Lesson Two
def remove_first_level1(tree):
    res = []

    for node in tree:
        if isinstance(node, list):
            for nested in node:
                res.append(nested)
    return res


# OR functional style by list comprehension
def remove_first_level2(tree):
    return [
        nested for node in tree if isinstance(node, list)
        for nested in node
    ]


# OR functional style by filter function
def remove_first_level3(tree):
    nested = filter(lambda node: isinstance(node, list), tree)
    return list(chain(*nested))
# END


# Lesson Three
# END


# Lesson Four
# END


# Lesson Five
# END


def main():
    pass


if __name__ == '__main__':
    main()
