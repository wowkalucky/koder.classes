# -*- encoding: utf-8 -*-

import sys
from p2_iter_lines import iter_lines
from p2_strip_spaces import strip_spaces
from p2_drop_empty import drop_empty
from p2_split_items import split_items


teststring = """
    123 asfd afsd df11
    asdf fdfg 2.0 asdf
    ad.sdf 6sd.f9sdf
    asdf 45 asdfasd 45fd
    2asdfa fds8"""


def get_ints(iter):
    """ Возращает из входного потока только целые """
    for item in iter:
        if isinstance(item, int):
            yield item


with open("test_file.txt", "r") as fd:
    assert list(get_ints(split_items(drop_empty(strip_spaces(iter_lines(fd))))))  == [1, 2, 3, 12]


if __name__ == '__main__':
    gen1 = iter_lines(open(sys.argv[0]))
    gen2 = strip_spaces(gen1)
    gen3 = drop_empty(gen2)
    gen4 = split_items(gen3)
    gen5 = get_ints(gen4)
    for line in gen5:
        print repr(line)
