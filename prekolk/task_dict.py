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