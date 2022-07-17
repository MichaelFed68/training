#!/usr/bin/env python3


from math import sqrt


# Solution Three
def calculate_distance(first_point, second_point):
   x1, y1, x2, y2 = [i if i > 0 else abs(i) for i in first_point + second_point]

   return sqrt(((x1 + x2) ** 2) + ((y1 + y2) ** 2))
# END


# Solution Four
# END


# Solution Five
# END


# Solution Six
# END


# Solution Seven
# END


def main():
    print('Запущено в качестве скрипта через интерпретатор')


if __name__ == '__main__':
    main()
