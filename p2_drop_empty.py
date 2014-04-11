# -*- encoding: utf-8 -*-
import sys
from p2_iter_lines import iter_lines
from p2_strip_spaces import strip_spaces


def drop_empty(iter):
    """
    Получает итератор и возвращает только непустые строки
    """
    for line in iter:
        if line != '':
            yield line


with open("test_file.txt", "r") as fd:
    assert list(drop_empty(strip_spaces(iter_lines(fd)))) == ['1 2 3 3.45 abra_cadabra', '12']


if __name__ == '__main__':
    gen1 = iter_lines(open(sys.argv[0]))
    gen2 = strip_spaces(gen1)
    gen3 = drop_empty(gen1)
    for line in gen3:
        print repr(line)
