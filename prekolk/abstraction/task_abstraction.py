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


def get_begin_point(segment):
    return segment['begin_point']


def get_end_point(segment):
    return segment['end_point']


def get_mid_point_of_segment(segment):
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)

    x = (get_x(begin_point) + get_x(end_point)) / 2
    y = (get_y(begin_point) + get_y(end_point)) / 2
    
    return make_decart_point(x, y)
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
