from random import shuffle

def deckGen() :
    x = list(range(1, 14)) # not include 14
    shuffle(x)

    for i in range(3):
        y =list(range(1, 14))
        shuffle(y)
        x.extend(y)

    shuffle(x)

    return x

op_map = {'+': 5, '-': 4, '*': 3, '/': 2, '(': -1}


def score(expr="10+11*12/13", goal=24):
    """
    Default argument example:
        "1+1+1+1" has 3 '+', so op_score = 5*3 = 15
        eval("1+1+1+1")=4, so diff = abs(4-24) = 20
        result = 15 - 20 = -5
    """
    global op_map
    try:
        diff = abs(eval(expr)-goal)
        op_score = sum([expr.count(op) * op_map[op] for op in op_map])
        return op_score - diff
    except:
        return -9999
