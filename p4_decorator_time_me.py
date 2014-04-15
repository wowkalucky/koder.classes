# -*- encoding: utf-8 -*-

"""
2)     Написать декоратор time_me, который делает профилирование функции,
        используя заданную функцию времени. Вторым параметром в time_me передается словарь,
        который нужно обновлять с каждым вызовом. В его елемент 'num_calls' нужно
        заносить количество вызовов, в его элемент 'cum_time' суммарное время.
"""

import time


statistic = {}

def time_me(time_fn, statdict):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            point1 = time_fn()
            res = fn(*args, **kwargs)
            point2 = time_fn()
            statdict['cum_time'] = statdict.setdefault('cum_time', 0.0) + (point2 - point1)
            statdict['num_calls'] = statdict.setdefault('num_calls', 0) + 1
            return res
        return wrapper
    return decorator


@time_me(time.time, statistic)
def some_func(x, y):
    time.sleep(1.1)
    return x + y


if __name__ == '__main__':
    # print "time.gmtime(0)", time.gmtime(0)
    # print "time.gmtime()", time.gmtime()
    # print "time.localtime()", time.localtime()
    # print "time.altzone", time.altzone
    # print "time.asctime()", time.asctime(time.gmtime(1000000000))
    # print "time.clock()", time.clock()
    # print "time.ctime", time.ctime(1000000000) == time.asctime(time.localtime(1000000000))
    # print "time.daylight", time.daylight
    # print "time.mktime", time.mktime(time.localtime())
    # print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())
    # print "time.time()", time.time()
    # print "time.timezone", time.timezone
    # print "time.tzname", time.tzname


    print some_func(4, 3), statistic
    print some_func(3, 3), statistic
    print some_func(2, 3), statistic
