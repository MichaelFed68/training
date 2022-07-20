#!/usr/bin/env python3

from math import sqrt


# Solution Three
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# END


# Solution Four
def make_decart_point(x, y):
    return {'x': x, 'y': y}


def get_x(point):
    return point['x']


def get_y(point):
    return point['y']


def make_segment(point1, point2):
    return {'begin_point': point1, 'end_point': point2}


def get_mid_point_of_segment(segment):
    x = (segment['begin_point']['x'] + segment['end_point']['x']) / 2
    y = (segment['begin_point']['y'] + segment['end_point']['y']) / 2
    return {'x': x, 'y': y}

def test_get_mid_point_of_segment():
    point1 = make_decart_point(3, 2)
    point2 = make_decart_point(0, 0)
    segment = make_segment(point1, point2)
    assert get_mid_point_of_segment(segment) == {'x': 1.5, 'y': 1}

test_get_mid_point_of_segment()
# END


# Solution Five
# END


# Solution Six
# END


# Solution Seven
# END


def main():
    print('Запущено в качестве скрипта через интерпретатор')


if __name__ == '__main__':
    main()
