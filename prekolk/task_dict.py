#!/usr/bin/env python3

# Soolution for lesson Two
def make_user (name, age):
    return {'name': name, 'age': age}
    
def format_user(user):
    return f"{user.get('name')}, {user.get('age')}"
# END


# Soolution for lesson Three
def count_all(date):
    dict = {}
    for i in date:
        if i in dict:
            continue
        count_keys = date.count(i)
        dict[i] = count_keys
    return dict
# END