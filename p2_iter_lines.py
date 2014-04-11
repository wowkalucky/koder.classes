# -*- encoding: utf-8 -*-
import sys


def iter_lines(fd):
    """
    Получает имя файла итерирует по строкам.
    Для чтения можно использовать только fd.read(1)
    """
    line = ''
    while True:
        s = fd.read(1)
        if s == "":
            break
        line += s
        if s == '\n':
            yield line[:-1]
            line = ''


with open("test_file.txt", "r") as fd:
    assert list(iter_lines(fd)) == ['1 2 3 3.45 abra_cadabra   ', '', '12']


if __name__ == '__main__':
    for line in iter_lines(open(sys.argv[0])):
        print repr(line)
