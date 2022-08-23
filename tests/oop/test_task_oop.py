from prekolk.oop import task_oop


def test_rgb2tuple():
    assert task_oop.rgb2tuple(task_oop.red) == (255, 0, 0)
    assert task_oop.rgb2tuple(task_oop.green) == (0, 255, 0)
    assert task_oop.rgb2tuple(task_oop.blue) == (0, 0, 255)


def test_Counter():
    counter = task_oop.Counter()
    assert counter.value == 0
    counter.increase(100)
    assert counter.value == 100
    counter.decrease(40)
    assert counter.value == 60
    counter.decrease(100)
    assert counter.value == 0
