# -*- encoding: utf-8 -*-

"""
1) Написать аналог встроенной функции map следующими способами:
 - рекурсивным (map_rq),
 - на генераторе (map_yield)
 - и рекурсивно на генераторе(map_rq_yield).

Рекурсивные функции должны обрабатывать не более одного элемента на шаг рекурсии.
Функции-генераторы должны обрабатывать элементы по мере запроса значений генератора.
"""

def map_yield(fn, iterable):
    for item in iterable:
        yield fn(item)


if __name__ == '__main__':
    print map(lambda x: x ** 2, xrange(5))
    print map_yield(lambda x: x ** 2, xrange(5))
    map_gen = map_yield(lambda x: x ** 2, xrange(5))
    for x in map_gen:
        print x
