# -*- encoding: utf-8 -*-

"""
интерпретатор подмножества языка forth
Программа на Forth состоит из набора команд(слов), некоторые из которых
имеют параметры. Для хранения данных используется стек - команды получают
свои операнды с вершины стека и туда же сохраняют результаты. В подмножестве
5 команд:
• put значение - помещает значение в стек. Значение может быть числом или
строкой. Строка заключается в кавычки, внутри строки кавычек быть не
может.
• pop - убирает значение из стека
• add - убирает из стека 2 значения, складывает их и помещает результат в
стек
• sub - убирает из стека 2 значения, вычитает их и помещает результат в
стек
• print - вынимает из стека 1 значение и печатает его.
1
2
put 3
put " asdaadasdas "

Каждая команда начинается с новой строки. Строки, начинающиеся с '#'
- комментарии. Ваша программа должна содержать функцию eval_forth(),
принимающую строку на языке forth и исполняющую ее. По умолчанию из
main вызывать eval_forth("example.frt") Пример, если в example.rft будет:
1
2
3
4
put 1
put 3
add
print
То программа должна напечатать '4'.
Сложение имеет такой же смысл, как и в питоне. Вычитание для строк не
определено Программа должна содержать функцию eval_forth(), принимающую
строку на языке forth и исполняющую ее. По умолчанию из main вызывать
eval_forth("example.frt")
"""
import string


STACK = []

def run_command(cmd_name, *args):
    def put(*arg):
        STACK.append(arg[0])

    locals()[cmd_name](args)



def validate(parts):
    commands = {'put': 1, 'pop': 0, 'add': 0, 'sub': 0, 'print': 0}
    if parts and parts[0] in commands:
        if len(parts[1:]) != commands[parts[0]]:
            raise TypeError, '"%s" takes exactly %d arguments (%d given)' % (
                parts[0], commands[parts[0]], len(parts[1:]))
        else:
            return True
    # etc
    return False


def parser(strng):
    def argparse(arg):
        if arg and arg[0] in string.digits:
            try:
                arg = int(arg)
            except:
                try:
                    arg = float(arg)
                except:
                    pass
        elif arg and arg[0] not in ["'", '"']:
            raise TypeError, 'Arguments must be int, float or string (in single or double quotes)'
        return arg

    strng = strng.rstrip('\n')
    parsed = {}
    if strng[0] == "#":
        parsed['type'] = 'comment'
        parsed['value'] = strng
        parsed['args'] = None
        return parsed

    parts = strng.split(" ")
    if validate(parts):
        parsed['type'] = 'command'
        parsed['value'] = parts[0]
        parsed['args'] = map(argparse, parts[1:])
        return parsed


def proc_line(line):
    parsed = parser(line)
    if parsed and parsed['type'] == 'command':
        command = parsed['value']
        args = parsed['args']
        print command, args
        print STACK
        run_command(command, args)
        print STACK


def eval_forth(filename):
    with open(filename, 'r') as fd:
        while True:
            line = fd.readline()
            if line == "":
                break
            proc_line(line)


if __name__ == '__main__':
    eval_forth("example.frt")
