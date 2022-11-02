#!/usr/bin/env python3

"""
Данный модуль демонстрирует простую библиотеку
для работы с графическими примитивами и дробями.
"""

import math


# Solution Three
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# END


# Solution Four and Five
def make_decart_point(x, y):
    # return {'x': x, 'y': y}
    return {
        'angle': math.atan2(y, x),
        'radius': math.sqrt(x ** 2 + y ** 2)
    }


def get_angle(point):
    return point['angle']


def get_radius(point):
    return point['radius']


def get_x(point):
    return round(get_radius(point) * math.cos(get_angle(point)))
    # return point['x']


def get_y(point):
    return round(get_radius(point) * math.sin(get_angle(point)))
    # return point['y']


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


# Solution Six
def make_rectangle(point, width, height):
    return {
        'start_point': point,
        'width': width,
        'height': height
    }


def get_start_point(rectangle):
    return rectangle['start_point']


def get_width(rectangle):
    return rectangle['width']


def get_height(rectangle):
    return rectangle['height']


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4


def my_contains_origin(rectangle):
    a = get_start_point(rectangle)

    x_from_width = get_x(a) + get_width(rectangle)
    y_from_height = get_y(a) - get_height(rectangle)

    b = make_decart_point(x_from_width, get_y(a))
    c = make_decart_point(get_x(a), y_from_height)
    d = make_decart_point(x_from_width, y_from_height)

    origin = set()
    for i in [a, b, c, d]:
        origin.add(get_quadrant(i))

    return len(origin) == 4
# OR


def contains_origin(rectangle):
    up_left = get_start_point(rectangle)
    down_right = make_decart_point(
        get_x(up_left) + get_width(rectangle),
        get_y(up_left) - get_height(rectangle),
    )

    return get_quadrant(up_left) == 2 and get_quadrant(down_right) == 4
# END


# Solution Seven
def make_rational(numer, denom):
    gcd_ = math.gcd(numer, denom)

    return {
        'numer': numer // gcd_,
        'denom': denom // gcd_
    }


def get_numer(fraction):
    return fraction['numer']


def get_denom(fraction):
    return fraction['denom']


def add_fractions(fraction1, fraction2):
    numer1 = get_numer(fraction1)
    denom1 = get_denom(fraction1)
    numer2 = get_numer(fraction2)
    denom2 = get_denom(fraction2)

    return make_rational(
        numer1 * denom2 + numer2 * denom1,
        denom1 * denom2
    )


def sub_fractions(fraction1, fraction2):
    numer1 = get_numer(fraction1)
    denom1 = get_denom(fraction1)
    numer2 = get_numer(fraction2)
    denom2 = get_denom(fraction2)

    return make_rational(
        numer1 * denom2 - numer2 * denom1,
        denom1 * denom2
    )


def rat_to_string(fraction):
    return f'{get_numer(fraction)}/{get_denom(fraction)}'
# END


def main():
    print('Запущено в качестве скрипта через интерпретатор')


if __name__ == '__main__':
    main()
