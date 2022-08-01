import pytest
from hexlet.fs import *
from prekolk.trees.tasks_trees import *


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


def test_du():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('nginx.conf', {'size': 800}),
            ]),
            mkdir('consul', [
                mkfile('.config.json', {'size': 1200}),
                mkfile('data', {'size': 8200}),
                mkfile('raft', {'size': 80}),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])

    expected = [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]

    assert du(tree) == expected
