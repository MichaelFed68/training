import pytest
from prekolk.abstraction.task_abstraction import *


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


def test_get_begin_point_and_get_end_point():
    point1 = make_decart_point(3, 2)
    point2 = make_decart_point(0, 0)
    segment = make_segment(point1, point2)
    assert get_begin_point(segment) == point1
    assert get_end_point(segment) == point2


def test_get_mid_point_of_segment():
    segment = make_segment(make_decart_point(3, 2), make_decart_point(1, -4))
    assert get_mid_point_of_segment(segment) == {'x': 2.0, 'y': -1.0}
