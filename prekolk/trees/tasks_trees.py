#!/usr/bin/env python3

from copy import deepcopy
from itertools import chain

from hexlet import fs


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
def generate():
    file_hierarchy = fs.mkdir('python-package', [
        fs.mkfile('Makefile.jpg', {'size': 50}),
        fs.mkfile('README.md'),
        fs.mkdir('dist'),
        fs.mkdir('tests', [
            fs.mkfile('test_solution.jpg', {'size': 50})
        ]),
        fs.mkfile('pyproject.toml'),
        fs.mkdir('.venv', [
            fs.mkdir('lib', [
                fs.mkdir('python3.6', [
                    fs.mkdir('site-packages', [
                        fs.mkfile('hexlet-python-package.jpg', {'size': 50})
                    ])
                ])
            ])
        ], {'owner': 'root', 'hidden': False})
    ], {'hidden': True})

    return file_hierarchy
# END


# Lesson Four
def compress_images(node):
    name = fs.get_name(node)
    new_meta = deepcopy(fs.get_meta(node))

    if fs.is_file(node):
        if name[-4:] == '.jpg':
            new_meta['size'] = new_meta['size'] // 2
            compressed = fs.mkfile(name, new_meta)
            return compressed
        else:
            return node

    children = fs.get_children(node)
    new_children = list(map(compress_images, children))

    new_nested_node = fs.mkdir(name, new_children, new_meta)
    return new_nested_node
# END


# Lesson Five
# END


def main():
    pass


if __name__ == '__main__':
    main()
