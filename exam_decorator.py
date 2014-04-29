#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Написать декоратор, реализующий случайную задержку перед вызовом декорируемой функции.
"""

import random
import time

__author__ = 'wowkalucky'


def wait(mix_time, min_time):
    def deco(fn):
        delay = random.randint(mix_time, min_time)
        def inner(*args, **kwargs):
            time.sleep(delay)
            return fn(*args, **kwargs)
        return inner
    return deco


@wait(1, 5)
def some_func(name="Lola"):
    print "Run, {}, run!".format(name)


if __name__=='__main__':
    some_func()
    some_func(name='Rabbit')








