#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реализовать функцию flatten получающую на вход список, часть элементов которого
могут быть списками или генераторами. flatten должна рекурсивно их раскрыть в одномерным
массив. При этом список или генератор заменяется на свои элементы в оригинальном массиве.
Примеры

flatten([1, 2, 3]) == [1, 2, 3]
flatten([1, 2, [3]]) == [1, 2, 3]
flatten([[1, 2], [1, 3]]) == [1, 2, 1, 3]
flatten([[1, [[[[2]]]], [1, [3, [[[[[4]]]]]]]]]) == [1, 2, 1, 3, 4]
"""

import copy
import collections

__author__ = 'wowkalucky'


def flatten(multilevel_list):
    """
    Gets multilevel list of objects
    -> flatten list of every level objects
    """
    for item in copy.deepcopy(multilevel_list):
        if isinstance(item, collections.Iterable):
            multilevel_list.remove(item)
            map(lambda x: multilevel_list.append(x), flatten(item))
    return multilevel_list


if __name__=='__main__':
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([1, 2, [3]]) == [1, 2, 3]
    assert flatten([[1, 2], [1, 3]]) == [1, 2, 1, 3]
    assert flatten([[1, [[[[2]]]], [1, [3, [[[[[4]]]]]]]]]) == [1, 2, 1, 3, 4]
