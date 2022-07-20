import pytest
from prekolk.abstraction.task_abstraction import calculate_distance
from prekolk.abstraction.task_abstraction import make_decart_point
from prekolk.abstraction.task_abstraction import get_x, get_y
from prekolk.abstraction.task_abstraction import make_segment
from prekolk.abstraction.task_abstraction import get_begin_point, get_end_point
from prekolk.abstraction.task_abstraction import get_mid_point_of_segment


def test_calculate_distance():
    assert calculate_distance([5, 2], [7, 8]) == 6.324555320336759
    assert calculate_distance([-5, 2], [-7, -8]) == 10.198039027185569


def test_with_empty_lists():
    with pytest.raises(ValueError):
        calculate_distance([], [])


def test_make_decart_point():
    assert make_decart_point(1, 4) == {'x': 1, 'y': 4}


def test_get_x_and_get_y():
    point = make_decart_point(1, 4)
    assert get_x(point) == 1
    assert get_y(point) == 4


def test_make_segment():
    point1 = make_decart_point(3, 2)
    point2 = make_decart_point(0, 0)
    dictionary = {'begin_point': point1, 'end_point': point2}
    assert make_segment(point1, point2) == dictionary


def test_get_mid_point_of_segment():
    segment = make_segment(make_decart_point(3, 2), make_decart_point(1, -4))
    assert get_mid_point_of_segment(segment) == {'x': 2.0, 'y': -1.0}
