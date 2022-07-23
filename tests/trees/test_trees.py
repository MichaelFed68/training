import pytest
from prekolk.trees.tasks_trees import *


@pytest.fixture
def trees():
    def inner():
        tree1 = [[5], 6, [1, 9]]
        tree2 = [[5], 6, [[1, 9]]]
        for tree in [tree1, tree2]:
            yield tree
    return inner


def test_remove_first_level1(trees):
    trees_gen = trees()
    assert remove_first_level1(next(trees_gen)) == [5, 1, 9]
    assert remove_first_level1(next(trees_gen)) == [5, [1, 9]]


def test_remove_first_level2(trees):
    trees_gen = trees()
    assert remove_first_level2(next(trees_gen)) == [5, 1, 9]
    assert remove_first_level2(next(trees_gen)) == [5, [1, 9]]


def test_remove_first_level3(trees):
    trees_gen = trees()
    assert remove_first_level3(next(trees_gen)) == [5, 1, 9]
    assert remove_first_level3(next(trees_gen)) == [5, [1, 9]]


def test_downcase_file_names():
    expected = {
        'name': 'python-package',
        'type': 'directory',
        'meta': {'hidden': True},
        'children': [
            {
                'name': 'Makefile',
                'type': 'file',
                'meta': {}
            },
            {
                'name': 'README.md',
                'type': 'file',
                'meta': {}
            },
            {
                'name': 'dist',
                'type': 'directory',
                'meta': {},
                'children': []
            },
            {
                'name': 'tests',
                'type': 'directory',
                'meta': {},
                'children': [
                    {
                        'name': 'test_solution.py',
                        'type': 'file',
                        'meta': {}
                    }
                ]
            },
            {
                'name': 'pyproject.toml',
                'type': 'file',
                'meta': {}
            },
            {
                'name': '.venv',
                'type': 'directory',
                'meta': {'owner': 'root', 'hidden': False},
                'children': [
                    {
                        'name': 'lib',
                        'type': 'directory',
                        'meta': {},
                        'children': [
                            {
                                'name': 'python3.6',
                                'type': 'directory',
                                'meta': {},
                                'children': [
                                    {
                                        'name': 'site-packages',
                                        'type': 'directory',
                                        'meta': {},
                                        'children': [
                                            {
                                                'name': 'hexlet-python-package.egg-link', # noqa
                                                'type': 'file',
                                                'meta': {}
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    assert generate() == expected
