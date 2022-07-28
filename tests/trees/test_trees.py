import pytest
from hexlet.fs import *
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
                                                'meta': {'size': 50}
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


def test_compress_images_simple():
    tree = mkdir(
        'my_doc',
        [
            mkfile('avatar.jpg', {'size': 100}),
            mkfile('photo.jpg', {'size': 150})
        ],
    {'hide': False},
    )

    expected = {
    'name': 'my_doc',
    'type': 'directory',
    'children': [
        {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
        {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
    ],
    'meta': {'hide': False},
    }

    assert compress_images(tree) == expected


def test_compress_images():
    tree = mkdir(
        'my documents',
        [
            mkdir('documents.jpg'),
            mkfile('avatar.jpg', {'size': 100}),
            mkfile('passport.jpg', {'size': 200}),
            mkfile('family.jpg', {'size': 150}),
            mkfile('addresses', {'size': 125}),
            mkdir('assets', [
                mkfile('lol.jpg', {'size': 200}),
                ],
            ),
        ],
        {'test': 'haha'},
    )

    expected = {
        'name': 'my documents',
        'children': [
            {
                'name': 'documents.jpg',
                'children': [],
                'meta': {},
                'type': 'directory',
            },
            {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
            {'name': 'passport.jpg', 'meta': {'size': 100}, 'type': 'file'},
            {'name': 'family.jpg', 'meta': {'size': 75}, 'type': 'file'},
            {'name': 'addresses', 'meta': {'size': 125}, 'type': 'file'},
            {
                'name': 'assets',
                'children': [
                    {
                        'name': 'lol.jpg',
                        'type': 'file',
                        'meta': {'size': 100},
                    },
                ],
                'meta': {},
                'type': 'directory',
            },
        ],
        'meta': {'test': 'haha'},
        'type': 'directory',
    }

    assert compress_images(tree) == expected


def test_compress_images_no_change():
    tree = mkdir('documents', [mkdir('presentations')])

    expected = {
        'name': 'documents',
        'type': 'directory',
        'meta': {},
        'children': [
            {
                'name': 'presentations',
                'type': 'directory',
                'meta': {},
                'children': [],
            },
        ],
    }

    assert compress_images(tree) == expected
