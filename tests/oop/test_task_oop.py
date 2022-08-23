from prekolk.oop import task_oop


def test_rgb2tuple():
    assert task_oop.rgb2tuple(task_oop.red) == (255, 0, 0)
    assert task_oop.rgb2tuple(task_oop.green) == (0, 255, 0)
    assert task_oop.rgb2tuple(task_oop.blue) == (0, 0, 255)
