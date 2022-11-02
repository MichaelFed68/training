import pytest

from training.compound_data import task_compound_data as cd


def test_get_symmetrical_point():
    neg_point = cd.main_abstr.make_decart_point(-1, -5)
    pos_point = cd.main_abstr.make_decart_point(1, 5)

    assert cd.get_symmetrical_point(neg_point) == cd.main_abstr.make_decart_point(1, 5)
    assert cd.get_symmetrical_point(pos_point) == cd.main_abstr.make_decart_point(-1, -5)
