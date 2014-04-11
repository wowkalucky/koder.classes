# -*- encoding: utf-8 -*-

"""
2)     Написать декоратор time_me, который делает профилирование функции,
        используя заданную функцию времени. Вторым параметром в time_me передается словарь,
        который нужно обновлять с каждым вызовом. В его елемент 'num_calls' нужно
        заносить количество вызовов, в его элемент 'cum_time' суммарное время.
    Пример использования:

    import time

    statistic = {}

    def time_me(time_func, statistic):
        .....

    @time_me(time.time, statistic)
    def som_func(x, y):
        time.sleep(1.1)

    time_me(1, 2)
    time_me(1, 2)

"""

import time

statistic = {}

assert statistic['num_calls'] == 2
assert 2.5 > statistic['cum_time'] > 2


def time_me(time_func, statistic):



if __name__ == '__main__':
    pass
