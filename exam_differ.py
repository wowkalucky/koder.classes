#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
diff для папок.

Функция получает два пути и сравнивает два дерева в файловой системе.
Возвращает множество пар вида ('+'/'-'/'*', путь). Где '+' означает, что
соответствующий объект есть во втором дереве, но отcутствует в первом,
'-' означает, что соответствующий объект есть во первом дереве, но отсутствует
во втором, '*' означает, что объект это файл, который есть в обоих деревьях,
но для него изменилось время модификации (st_mtime). Если объект изменил тип,
например файл в первом дереве и папка во втором, то необходимо выдать для
него две пары - ('-', path), ('+', path) в указанном порядке.
Путь возвращается относительный (от указанного корня). Если удалена папка,
то возвращаяется только одна пара ('-', path). Если папка созданна, то
возвращяется набор пар для всех объектов в папке, включая папка.
Операции над папками должны идти раньше операций над вложенными в них файлами
или папками. Содержимое файлов и атрибуты сравнивать не надо (за исключением
st_mtime, что описанно выше и для чего применяется '*').
"""
import os
import itertools

__author__ = 'wowkalucky'


def dir_diff(path1, path2):
    """
    Gets two absolute paths - strings,
    -> tuples set, as: (status, path)
    diff statuses:
        '+' - object appears in path2,
        '-' - object disappears in path2,
        '*' - object mutated
    """
    status = {
        'created': '+',
        'removed': '-',
        'changed': '*',
    }
    # TODO: check for trailing slash

    class Node(object):
        def __init__(self, path, type, parent=None, children=None):
            self.basepath, self.name = os.path.split(path)
            self.type = type
            self.parent = parent
            self.children = children

        def __str__(self):
            return "<< '%s' - %s >>" % (self.name, self.type)

    first_tree = [[]]
    second_tree = [[]]

    def parse(tree, dir, files):
        dirs = tree[0]
        parent_node = dirs[-1] if dirs else None
        node = Node(dir, "dir", parent=parent_node, children=files)
        # print "name:", node.name
        # print "type:", node.type
        # print "parent:", node.parent
        # print "children:", node.children
        # print "parent_node", parent_node
        dirs.append(node.name)
        tree.append(node)

    os.path.walk(path1, parse, first_tree)
    os.path.walk(path2, parse, second_tree)
    print "first_tree", first_tree
    print "second_tree", second_tree


#   TODO: осталось пройтись по дереву :) и вывести разницу - not enough time - game over





if __name__ == '__main__':
    path1 = "/home/wowkalucky/PycharmProjects/koder_school/testpathes/path1/"
    path2 = "/home/wowkalucky/PycharmProjects/koder_school/testpathes/path2/"
    dir_diff(path1, path2)

"""
.
├── path1
│   └── x
│       ├── f.txt
│       ├── y
│       │   └── c.txt
│       └── z.txt
└── path2
    └── x
        ├── f.txt
        ├── m
        │   └── c.txt
        ├── p.txt
        └── z.txt
            └── m.txt


вывод

    тут немного некорректно, но суть ясна
    ('-', 'x/m')
    ('+', 'x/y')
    ('+', 'x/y/c.txt')
    ('-', 'x/z.txt')
    ('+', 'x/z.txt')
    ('-', 'x/z.txt/m.txt')
    ('*', 'x/f.txt')
    ('+', 'x/p.txt')

"""
