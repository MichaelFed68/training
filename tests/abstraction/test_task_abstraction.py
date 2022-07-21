import pytest
from prekolk.abstraction.task_abstraction import *


def test_calculate_distance():
    assert calculate_distance([5, 2], [7, 8]) == 6.324555320336759
    assert calculate_distance([-5, 2], [-7, -8]) == 10.198039027185569


def test_with_empty_lists():
    with pytest.raises(ValueError):
        calculate_distance([], [])


def test_make_decart_point():
    assert make_decart_point(4, 8) == {
        'angle': 1.1071487177940904,
        'radius': 8.94427190999916
    }


def test_get_x_and_get_y():
    point = make_decart_point(4, 8)
    assert get_x(point) == 4
    assert get_y(point) == 8


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
    assert get_mid_point_of_segment(segment) == make_decart_point(2.0, -1.0)


def test_contains_origin():
    point1 = make_decart_point(0, 1)
    point2 = make_decart_point(-4, 3)

    rectangle = make_rectangle(point1, 4, 5)
    assert contains_origin(rectangle) is False

    rectangle1 = make_rectangle(point2, 5, 4)
    assert contains_origin(rectangle1) is True

    rectangle2 = make_rectangle(point2, 5, 2)
    assert contains_origin(rectangle2) is False


def test_make_rational():
    assert make_rational(3, 9) == {'numer': 1, 'denom': 3}


@pytest.fixture
def fraction1():
    return make_rational(3, 9)


@pytest.fixture
def fraction2():
    return make_rational(10, 3)


@pytest.fixture
def fraction3():
    return make_rational(10, 4)


def test_get_numer_and_get_dennom(fraction1):
    assert get_numer(fraction1) == 1
    assert get_denom(fraction1) == 3


def test_rat_to_string(fraction1, fraction3):
    assert rat_to_string(fraction1) == '1/3'
    assert rat_to_string(fraction3) == '5/2'
    assert rat_to_string(make_rational(-1, 3)) == '-1/3'


def test_add_fractions(fraction1, fraction2, fraction3):
    assert add_fractions(fraction1, fraction2) == make_rational(11, 3)
    assert add_fractions(fraction1, fraction3) == make_rational(17, 6)


def test_sub_fractions(fraction1, fraction2, fraction3):
    assert sub_fractions(fraction1, fraction2) == make_rational(-9, 3)
    assert sub_fractions(fraction1, fraction3) == make_rational(-13, 6)
