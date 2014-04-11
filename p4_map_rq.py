# -*- encoding: utf-8 -*-

"""
1) Написать аналог встроенной функции map следующими способами:
 - рекурсивным (map_rq),
 - на генераторе (map_yield)
 - и рекурсивно на генераторе(map_rq_yield).

Рекурсивные функции должны обрабатывать не более одного элемента на шаг рекурсии.
Функции-генераторы должны обрабатывать элементы по мере запроса значений генератора.
"""

# map()
def map_rq(fn, iterable):







# assert map(lambda x: x ** 2, range(5)) == [0, 1, 4, 9, 16]
# assert map_rq(lambda x: x ** 2, range(5)) == [0, 1, 4, 9, 16]

if __name__ == '__main__':
    # print map_rq(lambda x: x ** x, range(5))

    print map(lambda x: x ** 2, range(5))
    print map(lambda x: x ** 2, xrange(5))
