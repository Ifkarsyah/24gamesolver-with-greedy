from itertools import combinations_with_replacement
from tools import score
from algo_bf import solve_bforce


all_input = combinations_with_replacement(range(1, 14), 4)
all_input = [sorted(inp, reverse=True) for inp in all_input]


def main_bf():
    global all_input
    all_answer_bf = [solve_bforce(inp, 24) for inp in all_input]
    all_score_bf = [score(expr) for expr in all_answer_bf]
    zip_result = zip(all_input, all_answer_bf, all_score_bf)
    return list(zip_result)
