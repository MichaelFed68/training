#!/usr/bin/env python3
from collections import defaultdict


# Soolution for lesson Two
def make_user(name, age):
    return {'name': name, 'age': age}


def format_user(user):
    return f"{user.get('name')}, {user.get('age')}"
# END


# Soolution for lesson Three
def count_all(items):
    dict = {}
    for i in items:
        if i in dict:
            continue
        dict[i] = items.count(i)
    return dict
# END


# Soolution for lesson Four
def collect_indexes(items):
    result = defaultdict(list)

    if type(items) == dict:
        for key, value in items.items():
            result[value].append(key)
        return result

    for index, elem in enumerate(items):
        result[elem].append(index)
    return result
# END


# Solution for lesson Five
def all_unique(items):
    list_items = list(items)
    return len(list_items) == len(set(list_items))
# END


def main():
    lis = [2929, 'FFF,', 19, 10]
    print(all_unique(lis))


if __name__ == '__main__':
    main()
