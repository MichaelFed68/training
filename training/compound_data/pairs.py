def cons(obj1, obj2):
    return obj1, obj2


def car(cons):
    return cons[0]


def cdr(cons):
    return cons[-1]


def is_pair(pair):
    if isinstance(pair, tuple):
        if len(pair) == 2:
            return True
    return False


def reverse_pair(pair):
    new_obj1 = cdr(pair)
    new_obj2 = car(pair)
    return cons(new_obj1, new_obj2)


def sum_of_pairs(pair1, pair2):
    sum_of_obj1 = car(pair1) + car(pair2)
    sum_of_obj2 = cdr(pair1) + cdr(pair2) 
    return cons(sum_of_obj1, sum_of_obj2)


def find_primitive_pair(pair):
    filtered_pairs = [i for i in pair if is_pair(i)]

    if filtered_pairs == []:
        return pair
    else:
        for pair in filtered_pairs:
            return find_primitive_pair(pair)


def main():
    pass


if __name__ == '__main__':
    main()
