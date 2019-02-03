def score(expr="1+1+1+1", goal=24):
    """
    Default argument example:
        "1+1+1+1" has 3 '+', so op_score = 5*3 = 15
        eval("1+1+1+1")=4, so diff = abs(4-24) = 20
        result = 15 - 20 = -5
    """
    op_map = {'+': 5, '-': 4, '*': 3, '/': 2, '(': -1}
    diff = abs(eval(expr)-goal)
    op_score = sum([expr.count(op) * op_map[op] for op in op_map])
    return op_score - diff


def solve(input=[1, 2, 3, 4], goal=24):
    """
    Greedy Algorithm:
        1. Prioritize by numbers
        2. Prioritize by operator
    """
    return "1+1+1+1"


def main():
    """
        1. Read Input, convert to int, and sort descending
        2. Solve for expression
        3. return expr to "out.txt"
    """
    with open('in.txt') as fin:
        inp = sorted(map(int, fin.read().split()), reverse=True)
    expr = solve(inp, 24)
    with open("out.txt", "w") as fout:
        fout.write(expr)

if __name__ == "__main__":
    main()
