#!/usr/bin/env python3

# Solution lesson Two
from operator import itemgetter


def get_odds(x):
    itemgetter(slice(None, None, 2))


def get_odds_2(x):
    return x[::2]


def odds_from_odds(list_of_lists):
    return list(map(get_odds, get_odds(list_of_lists)))


def keep_odds_from_odds(list_of_lists):
    del list_of_lists[1::2]
    for item in list_of_lists:
        del item[1::2]
# END


# Solution lesson Three
def non_empty_truths(list_of_lists):
    return [
        truth for truth in [
            [item for item in list_ if item]
            for list_ in list_of_lists
        ]
        if truth
    ]
# END


# Solution lesson Four
def number_of_unique_letters(str_):
    return len({char for char in str_.lower() if char.isalpha()})
# END


# Solution lesson Five
def is_int(x):
    return isinstance(x, int)


def each2d(test, matrix):
    return all(
        all(test(item) for item in row)
        for row in matrix
    )


def somy2d(test, matrix):
    return any(
        any(test(item) for item in row)
        for row in matrix
    )


def sum2d(test, matrix):
    return sum(
        sum(item for item in row if test(item))
        for row in matrix
    )
# END


# Solution lesson Six

# END


def main():
    print('q')


if __name__ == '__main__':
    main()
