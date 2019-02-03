def bracketting(expr, typ=11):
    if typ == 0:
        expr.insert(0, '(')
        expr.insert(4, ')')
        expr.insert(7, ')')
    elif typ == 1:
        expr.insert(0, '(')
        expr.insert(3, '(')
        expr.insert(7, '))')
    elif typ == 2:
        expr.insert(0, '(')
        expr.insert(4, ')')
        expr.insert(6, '(')
        expr.insert(10, ')')
    elif typ == 3:
        expr.insert(2, '((')
        expr.insert(6, ')')
        expr.insert(9, ')')
    elif typ == 4:
        expr.insert(2, '(')
        expr.insert(5, '(')
        expr.insert(9, '))')
    elif typ == 5:
        expr.insert(0, '(')
        expr.insert(6, ')')
    elif typ == 6:
        expr.insert(2, '(')
        expr.insert(8, ')')
    elif typ == 7:
        expr.insert(0, '(')
        expr.insert(4, ')')
    elif typ == 8:
        expr.insert(2, '(')
        expr.insert(6, ')')
    elif typ == 9:
        expr.insert(4, '(')
        expr.insert(8, ')')
    elif typ == 10:
        pass
    return ''.join(expr)


def score(expr="10+11*12/13", goal=24):
    """
    Default argument example:
        "1+1+1+1" has 3 '+', so op_score = 5*3 = 15
        eval("1+1+1+1")=4, so diff = abs(4-24) = 20
        result = 15 - 20 = -5
    """
    op_map = {'+': 5, '-': 4, '*': 3, '/': 2, '(': -1}
    try:
        diff = abs(eval(expr)-goal)
        op_score = sum([expr.count(op) * op_map[op] for op in op_map])
        return op_score - diff
    except:
        return -9999
