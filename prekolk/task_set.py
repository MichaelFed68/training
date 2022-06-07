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


# Solution for lesson Seven
def diff_keys(old, new):
    o, n = set(old), set(new)
    return {
        'kept': o & n,
        'added': n - o,
        'removed': o - n
    }
# OR
def another_diff_keys(old, new):
    return {
        'kepts': old.keys() & new.keys(),
        'added': new.keys() - old.keys(),
        'removed': old.keys() - new.keys()
    }
# END


# Solution for lesson Eigth

# END


def main():
    n = {'name': 'Bob', 'age': 21}
    s = {'name': 'Bob', 'lol': 1}
    print(another_diff_keys(s, n))  

if __name__ == '__main__':
    main()