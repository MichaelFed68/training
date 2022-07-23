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
