from prekolk.oop import task_oop


def test_rgb2tuple():
    assert task_oop.rgb2tuple(task_oop.red) == (255, 0, 0)
    assert task_oop.rgb2tuple(task_oop.green) == (0, 255, 0)
    assert task_oop.rgb2tuple(task_oop.blue) == (0, 0, 255)


def test_CounterOne():
    counter = task_oop.CounterOne()

    assert counter.value == 0
    counter.increase(100)
    assert counter.value == 100
    counter.decrease(40)
    assert counter.value == 60
    counter.decrease(100)
    assert counter.value == 0


def test_CounterTwo():
    instance1 = task_oop.CounterTwo()
    instance2 = instance1.increase().increase(9).decrease(5)
    instance3 = instance2.decrease(10)

    assert instance1 is not instance2
    assert instance1.value == 0
    assert instance2.value == 5
    assert instance3.value == 0


def test_HourClock():
    clock = task_oop.HourClock()

    clock.hours = 10
    assert clock.hours == 10
    clock.hours = -1
    assert clock.hours == 11
    clock.hours = 123
    assert clock.hours == 3
