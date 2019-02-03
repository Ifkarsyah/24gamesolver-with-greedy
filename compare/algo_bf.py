from itertools import combinations_with_replacement, permutations
from tools import bracketting, score


def solve_bforce(inp=[10, 11, 12, 13], goal=24):
    """
        Give expression that give max possible score.
        solve_bf([10,11,12,13]) ==> '10+12+13-11'
    """
    max_expr = max(generate_all_expr(inp), key=score)
    return max_expr


def generate_all_expr(inp=[10, 11, 12, 13]):
    """
        generate(inp=[10,11,12,13]) ==> [[((,10,+,11,),+,12,),+13,...]]
    """
    op = "+-*/"
    all_op = list(combinations_with_replacement(op, 3))
    all_num = list(permutations(inp, len(inp)))
    all_expr = []
    for op in all_op:
        for num in all_num:
            merge_op_num = f_merge_opnum(num, op)
            bracket_expr(merge_op_num, all_expr)
    return all_expr


def bracket_expr(merge_op_num, all_expr):
    """
        Expand [1,+,2,*,3,/,4] to [[((,1,+,2,),+,3,),+4,... and 10 others]]
    """
    for i in range(0, 11):
        expr = merge_op_num[:]
        expr = bracketting(expr, i)
        all_expr.append(expr)


def f_merge_opnum(num, op):
    """
        f_merge([1,2,3,4],"+*/") ==> [1,+,2,*,3,/,4]
    """
    merge_op_num = list(num[:])
    for i in range(0, 3):
        merge_op_num.insert(i*2+1, op[i])
    merge_op_num = list(map(str, merge_op_num))
    return merge_op_num
