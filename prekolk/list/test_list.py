#!/usr/bin/env python3

# Testing Two
def build_query_string(items):
    list = []

    for k, v in items.items():
        list.append(f'{k}={v}')

    return '&'.join(sorted(list))
# END
