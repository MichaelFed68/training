#!/usr/bin/env python3
import os
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
                        fs.mkfile('hexlet-python-package.jpg', {'size': 49})
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

    if fs.is_file(node) and name.endswith('.jpg'):
        new_meta['size'] = new_meta['size'] // 2
        return fs.mkfile(name, new_meta)

    elif fs.is_file(node):
        return fs.mkfile(name, new_meta)

    children = fs.get_children(node)
    new_children = [compress_images(child) for child in children]
    return fs.mkdir(name, new_children, new_meta)
# END


# Lesson Five
def downcase_file_names(tree):
    name = fs.get_name(tree)
    new_meta = fs.get_meta(tree)

    if fs.is_file(tree):
        return fs.mkfile(name.lower(), new_meta)

    children = fs.get_children(tree)
    new_children = [downcase_file_names(child) for child in children]
    return fs.mkdir(name, new_children, new_meta)
# END


# Lesson six
def get_hidden_files_count1(tree):
    name = fs.get_name(tree)
    if fs.is_file(tree) and name.startswith('.'):
        return 1
    elif fs.is_directory(tree):
        children = fs.get_children(tree)
        hidden_files_count = sum(map(get_hidden_files_count1, children))
        return hidden_files_count
    return 0
# OR


def is_hidden_file(node):
    return fs.is_file(node) and fs.get_name(node).startswith('.')


def get_hidden_files_count2(tree):
    if fs.is_file(tree):
        return 1 if is_hidden_file(tree) else 0
    children = fs.get_children(tree)
    hidden_files_count = sum(map(get_hidden_files_count2, children))

    return hidden_files_count
# END


# Lesson Seven
def get_total_size(node):

    if fs.is_file(node):
        return fs.get_meta(node).get('size', 0)
    children = fs.get_children(node)
    size_children = sum(get_total_size(child) for child in children)
    return size_children


def du(tree):
    children = fs.get_children(tree)
    unsized_items = map(
        lambda child: (fs.get_name(child), get_total_size(child)),
        children,
    )
    return sorted(unsized_items, key=lambda item: item[1], reverse=True)
# END


# Lesson Eight
def find_files_by_name(tree, substring):

    def walk(node, path):
        name = fs.get_name(node)
        ancestry = os.path.join(path, name)
        if fs.is_file(node):
            if substring in name:
                return ancestry
            return []
        children = fs.get_children(node)
        matches = (walk(child, ancestry) for child in children)
        return fs.flatten(matches)

    return walk(tree, '')
# END


def main():
    pass


if __name__ == '__main__':
    main()
