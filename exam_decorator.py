#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Написать декоратор, реализующий случайную задержку перед вызовом декорируемой функции.
"""

import random
import time

__author__ = 'wowkalucky'


def wait(min_time, max_time):
    """ min_time, max_time - waiting limits (ints) """
    def deco(fn):
        def inner(*args, **kwargs):
            delay = random.randint(min_time, max_time)  # why only integers???
            time.sleep(delay)
            return fn(*args, **kwargs)
        return inner
    return deco


@wait(1, 10)
def some_func(name="Lola"):
    print "Run, {}, run!".format(name)
    return True


if __name__=='__main__':
    some_func()
    some_func(name='Rabbit')








