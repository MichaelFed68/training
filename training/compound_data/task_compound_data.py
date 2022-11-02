"""
Данный модуль демонстрирует расширенную версию библиотеки
для работы с графическими примитивами и дробями.

Основана на базовой библиотеке и пользуется ее предасталяемым
интерфейсом через импортированный модуль 'main_abstr'. 
"""

import math

import training.abstraction.task_abstraction as main_abstr


def get_symmetrical_point(point):
    x = main_abstr.get_x(point)
    y = main_abstr.get_y(point)

    if x < 0:
        x = abs(x)
    if y < 0:
        y = abs(y)
    else:
        x = -abs(x)
        y = -abs(y)

    return main_abstr.make_decart_point(x, y)
