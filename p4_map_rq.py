# -*- encoding: utf-8 -*-

"""
1) Написать аналог встроенной функции map следующими способами:
 - рекурсивным (map_rq),
 - на генераторе (map_yield)
 - и рекурсивно на генераторе(map_rq_yield).

Рекурсивные функции должны обрабатывать не более одного элемента на шаг рекурсии.
Функции-генераторы должны обрабатывать элементы по мере запроса значений генератора.
"""

def map_rq_naive(fn, iterable):
    assert isinstance(iterable, (list, tuple))
    if len(iterable) < 2:
        return [fn(iterable[0])]
    else:
        return [fn(iterable[0])] + map_rq(fn, iterable[1:])


def map_rq(fn, iterable):
    i = iter(iterable)     # this can be done much simpler
    try:
        _next = next(i)
    except StopIteration:
        return []
    else:
        return [fn(_next)] + map_rq(fn, i)


if __name__ == '__main__':
    print "map",  map(lambda x: x ** 2, xrange(5))
    print "map_rq_naive", map_rq_naive(lambda x: x ** 2, [0,1,2,3,4])
    print "map_rq", map_rq(lambda x: x ** 2, xrange(5))
