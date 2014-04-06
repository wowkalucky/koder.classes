# -*- encoding: utf-8 -*-

import sys
from p2_drop_empty import drop_empty
from p2_get_ints import get_ints
from p2_iter_lines import iter_lines
from p2_split_items import split_items
from p2_strip_spaces import strip_spaces

teststring = """
    123 asfd afsd df11
    asdf fdfg 2.0 asdf
    ad.sdf 6sd.f9sdf
    asdf 45 asdfasd 45fd
    2asdfa fds8"""

def my_sum(iter):
    """ Считает сумму элементов целых во входном потоке """
    total_sum = 0
    for item in iter:
        total_sum += item
        yield total_sum


if __name__ == '__main__':
    gen1 = iter_lines(open(sys.argv[0]))
    gen2 = strip_spaces(gen1)
    gen3 = drop_empty(gen2)
    gen4 = split_items(gen3)
    gen5 = get_ints(gen4)
    gen6 = my_sum(gen5)
    for line in gen6:
        print repr(line)
