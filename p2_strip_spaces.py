# -*- encoding: utf-8 -*-
import sys
from p2_iter_lines import iter_lines


def strip_spaces(iter):
    """
    Принимает итератор, получает из него строки и возвращает
    строки без стартовых и финальных пробельных символов
    """
    while iter:
        yield iter.next().strip()


with open("test_file.txt", "r") as fd:
    assert list(strip_spaces(iter_lines(fd))) == ['1 2 3 3.45 abra_cadabra', '', '12']


if __name__ == '__main__':
    gen1 = iter_lines(open(sys.argv[0]))
    gen2 = strip_spaces(gen1)
    for line in gen2:
        print repr(line)
