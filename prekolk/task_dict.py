#!/usr/bin/env python3

# Soolution for lesson Two
def make_user (name, age):
    return {'name': name, 'age': age}
    
def format_user(user):
    return f"{user.get('name')}, {user.get('age')}"
#END
