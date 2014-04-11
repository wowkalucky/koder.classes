# -*- encoding: utf-8 -*-

import sys
import string
from p2_iter_lines import iter_lines
from p2_strip_spaces import strip_spaces
from p2_drop_empty import drop_empty


def split_items(iter):
    """
    Получает итератор, считывает из него строки, разбивает их по
    пробелам и для каждого элемента определяет является ли он строковым
    представлением целого или числа с плавающей запятой. Приводит опознанные
    елементы к int/float соответсвенно, остальные оставляет строками.
    Возращает итератор по этим элементам
    """
    for line in iter:
        elements = line.split(" ")
        processed_els = []
        for el in elements:
            res = ''
            if el and el[0] in string.digits:
                try:
                    if '.' in el:
                        res = float(el)
                    else:
                        res = int(el)
                except ValueError:
                    pass
                else:
                    el = res
            processed_els.append(el)
        for pel in processed_els:
            yield pel


with open("test_file.txt", "r") as fd:
    assert list(split_items(drop_empty(strip_spaces(iter_lines(fd))))) == [1, 2, 3, 3.45, 'abra_cadabra', 12]


if __name__ == '__main__':
    gen1 = iter_lines(open(sys.argv[0]))
    gen2 = strip_spaces(gen1)
    gen3 = drop_empty(gen2)
    gen4 = split_items(gen3)
    for line in gen4:
        print repr(line)
