

def solve_greedy(inp=[10, 11, 12, 13], goal=24):
    inp.sort(reverse=True)
    expr = str(inp[0])
    size = len(inp)
    for i in range(1, size):
        candidate = []
        candidate.append(('+' + str(inp[i]), 5))
        candidate.append(('-' + str(inp[i]), 4))
        candidate.append(('*' + str(inp[i]), 3))
        candidate.append(('/' + str(inp[i]), 2))
        expr_add_cand = [expr + c[0] for c in candidate]
        exprcand_plus_op = [expr + c[0] + "+" + str(c[1]) for c in candidate]
        exprcand_min24 = [ec + "-24" for ec in exprcand_plus_op]
        exprcand_eval = [abs(eval(c)) for c in exprcand_min24]
        expr_min_idx = exprcand_eval.index(min(exprcand_eval))
        expr += candidate[expr_min_idx][0]
    return expr
