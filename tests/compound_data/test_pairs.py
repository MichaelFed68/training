from training.compound_data import pairs


def test_reverse_pair():
    pair = pairs.cons('one', 'two')
    expected = pairs.cons('two', 'one')

    assert pairs.reverse_pair(pair) == expected


def test_sum_of_pair():
    pair1 = pairs.cons(4, 10)
    pair2 = pairs.cons(100, 0)
    expected = pairs.cons(104, 10)

    assert pairs.sum_of_pairs(pair1, pair2) == expected


def test_find_primitive_pair():
    pair2 = pairs.cons(pairs.cons(None, pairs.cons(1, 5)), None)
    expected = pairs.cons(1, 5)
    assert pairs.find_primitive_pair(pair2) == expected
