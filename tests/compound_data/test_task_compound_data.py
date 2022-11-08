from training.compound_data import task_compound_data as cd


def test_get_symmetrical_point():
    neg_point = cd.main_abstr.make_decart_point(-1, -5)
    pos_point = cd.main_abstr.make_decart_point(1, 5)

    assert cd.get_symmetrical_point(neg_point) == pos_point
    assert cd.get_symmetrical_point(pos_point) == neg_point


def test_get_middle():
    segment = cd.make_segment(cd.make_point(1, 2), cd.make_point(-4, -2))
    expected = cd.make_point(-1.5, 0)

    assert cd.get_middle(segment) == expected
