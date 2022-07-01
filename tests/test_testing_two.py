from prekolk.testing.tasks_for_tests import get_function as get



if get({'a': 1, 'b':2, 'c': 3}, 'b', 'default_value') != 2:
    raise Exception('Тесты закончились с ошибкой 0/2')
if get({}, 'b', 'default_value') != 'default_value':
    raise Exception('Тесты закончились с ошибкой 0/2')
if get({'a': 1, 'b':2, 'c': 3}, 'e', 'default_value') != 'default_value':
    raise Exception('Тесты закончились с ошибкой 1/2')

print('Успешно 2/2')
