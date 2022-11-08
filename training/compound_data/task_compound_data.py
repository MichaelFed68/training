"""
Данный модуль демонстрирует расширенную версию библиотеки
для работы с графическими примитивами и дробями.

Основана на базовой библиотеке и пользуется ее предасталяемым
интерфейсом через импортированный модуль 'main_abstr'.
"""

import training.abstraction.task_abstraction as main_abstr
from training.compound_data import pairs


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


# Уровень абстракции для работы с сущностью "точка"
# Begin
def make_point(x, y):
    return pairs.cons(x, y)


def get_x(point):
    return pairs.car(point)


def get_y(point):
    return pairs.cdr(point)


def to_string(point):
    return str(point)
# End
