import pytest
from hexlet.fs import *
from training.trees.tasks_trees import *


@pytest.fixture
def trees_level():
    def inner():
        tree1 = [[5], 6, [1, 9]]
        tree2 = [[5], 6, [[1, 9]]]
        for tree in [tree1, tree2]:
            yield tree
    return inner


def test_remove_first_level1(trees_level):
    trees_gen = trees_level()
    assert remove_first_level1(next(trees_gen)) == [5, 1, 9]
    assert remove_first_level1(next(trees_gen)) == [5, [1, 9]]


def test_remove_first_level2(trees_level):
    trees_gen = trees_level()
    assert remove_first_level2(next(trees_gen)) == [5, 1, 9]
    assert remove_first_level2(next(trees_gen)) == [5, [1, 9]]


def test_remove_first_level3(trees_level):
    trees_gen = trees_level()
    assert remove_first_level3(next(trees_gen)) == [5, 1, 9]
    assert remove_first_level3(next(trees_gen)) == [5, [1, 9]]


@pytest.fixture
def tree():
    tree = fs.mkdir('python-package', [
        fs.mkfile('Makefile.jpg', {'size': 50}),
        fs.mkfile('.README.md'),
        fs.mkdir('dIst'),
        fs.mkdir('tests', [
            fs.mkfile('test_solution.jpg', {'size': 50})
        ]),
        fs.mkfile('pyproject.toml'),
        fs.mkdir('.venv', [
            fs.mkdir('lib', [
                fs.mkdir('pythoN3.6', [
                    fs.mkdir('site-packages', [
                        fs.mkfile('.hexlet-pythoN-package.jpg', {'size': 49})
                    ])
                ])
            ])
        ], {'owner': 'root', 'hidden': False})
    ], {'hidden': True})

    return tree


def test_generate():
    expected = {
        'name': 'python-package',
        'type': 'directory',
        'meta': {'hidden': True},
        'children': [
            {
                'name': 'Makefile.jpg',
                'type': 'file',
                'meta': {'size': 50}
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
                        'name': 'test_solution.jpg',
                        'type': 'file',
                        'meta': {'size': 50}
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
                                                'name': 'hexlet-python-package.jpg', # noqa
                                                'type': 'file',
                                                'meta': {'size': 49}
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


def test_compress_images(tree):
    expected = {
        'name': 'python-package',
        'type': 'directory',
        'meta': {'hidden': True},
        'children': [
            {
                'name': 'Makefile.jpg',
                'type': 'file',
                'meta': {'size': 25}
            },
            {
                'name': '.README.md',
                'type': 'file',
                'meta': {}
            },
            {
                'name': 'dIst',
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
                        'name': 'test_solution.jpg',
                        'type': 'file',
                        'meta': {'size': 25}
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
                                'name': 'pythoN3.6',
                                'type': 'directory',
                                'meta': {},
                                'children': [
                                    {
                                        'name': 'site-packages',
                                        'type': 'directory',
                                        'meta': {},
                                        'children': [
                                            {
                                                'name': '.hexlet-pythoN-package.jpg', # noqa
                                                'type': 'file',
                                                'meta': {'size': 24}
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

    assert compress_images(tree) == expected


def test_downcase_file_names(tree):
    expected = {
        'name': 'python-package',
        'type': 'directory',
        'meta': {'hidden': True},
        'children': [
            {
                'name': 'makefile.jpg',
                'type': 'file',
                'meta': {'size': 50}
            },
            {
                'name': '.readme.md',
                'type': 'file',
                'meta': {}
            },
            {
                'name': 'dIst',
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
                        'name': 'test_solution.jpg',
                        'type': 'file',
                        'meta': {'size': 50}
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
                                'name': 'pythoN3.6',
                                'type': 'directory',
                                'meta': {},
                                'children': [
                                    {
                                        'name': 'site-packages',
                                        'type': 'directory',
                                        'meta': {},
                                        'children': [
                                            {
                                                'name': '.hexlet-python-package.jpg', # noqa
                                                'type': 'file',
                                                'meta': {'size': 49}
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

    assert downcase_file_names(tree) == expected


def test_get_hidden_files_count1(tree):
    assert get_hidden_files_count1(tree) == 2


def test_get_hidden_files_count2(tree):
    assert get_hidden_files_count2(tree) == 2


def test_du(tree):
    expected = [
        ('Makefile.jpg', 50),
        ('tests', 50),
        ('.venv', 49),
        ('.README.md', 0),
        ('dIst', 0),
        ('pyproject.toml', 0),
    ]
    assert du(tree) == expected


def test_find_files_by_name(tree):
    expected = [
        'python-package/Makefile.jpg',
        'python-package/tests/test_solution.jpg',
        'python-package/.venv/lib/pythoN3.6/site-packages/.hexlet-pythoN-package.jpg', # noqa
    ]
    assert find_files_by_name(tree, '.jpg') == expected
