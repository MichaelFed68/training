from prekolk.dict_and_set.task_dict import all_unique


if all_unique([2929, 'FFF,', 19, 10]) != True:
    raise Exception('Ошибка')
print('Успешно')
