# -*- encoding: utf-8 -*-
import sys
from p2_iter_lines import iter_lines


def drop_empty(iter):
    """
    Получает итератор и возвращает только непустые строки
    """
    for line in iter:
        if line != '\n':
            yield line


if __name__ == '__main__':
    gen1 = iter_lines(open(sys.argv[0]))
    gen2 = drop_empty(gen1)
    for line in gen2:
        print repr(line)
