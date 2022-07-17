import pytest
from prekolk.abstraction.task_abstraction import calculate_distance


def test_calculate_distance():
    assert calculate_distance([0, 0], [3, 4]) == 5.0
    assert calculate_distance([5, 2], [7, 8]) == 15.620499351813308
    assert calculate_distance([-5, 2], [-7, -8]) == 15.620499351813308


def test_with_empty_lists():
    with pytest.raises(ValueError):
        calculate_distance([], [])
