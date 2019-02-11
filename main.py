from front_end_2 import *
from algo import *


def main():
    inp = input_from_file()
    expr = solve_greedy(inp, 24)
    output_to_file(expr)

if __name__ == "__main__":
    main()
