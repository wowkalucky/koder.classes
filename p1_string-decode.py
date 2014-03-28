#-*- encoding: utf-8 -*-

def decode(strng):
    """
    Нужно преобразовать строку по следующим правилам:
    • Если символ идет 2 и больше раз подрят - записать его в результат 1 раз
    • Если символ повторяется 1 раз - отбросить
    • Если # повторяется два и более раз - последний символ, записанный в
    результат записать еще раз
    """
    if len(strng) < 2:
        return ""

    def process_memory(symbol, res, memdict):
        candidate, repited = memdict.items()[0]
        memdict.clear()
        memdict[symbol] = 1
        if repited > 1:
            if candidate == special:
                if res:
                    res.append(res[-1])
            else:
                res.append(candidate)

    special = '#'
    memdict = {}
    res = []
    for symbol in strng:
        if memdict:
            if symbol in memdict.keys():
                memdict[symbol] += 1
            else:
                process_memory(symbol, res, memdict)

        else:
            memdict[symbol] = 1
    process_memory(symbol, res, memdict)
    return "".join(res)


assert decode("") == ""
assert decode("1") == ""
assert decode("11") == "1"
assert decode("11111") == "1"
assert decode("11#") == "1"
assert decode("11122234###55") == "1225"
assert decode("11##") == "11"

assert decode("###") == ""
assert decode("###1") == ""
assert decode("###111") == "1"
assert decode("###111222") == "12"
assert decode("###1112223#") == "12"
assert decode("###1112223#444##55616666") == "124456"
assert decode("###1112223#444##55616666#") == "124456"
assert decode("###1112223#444##55616666###") == "1244566"
