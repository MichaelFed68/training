#!/usr/bin/env python3

# Soolution for lesson Two
def make_user (name, age):
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
from collections import defaultdict

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