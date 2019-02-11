from front_end_2 import *
from algo import *


def main():
    """
        How to run:
            1. Prepare "in.txt" and "out.txt"
            2. Insert your input in "in.txt" with format "1 2 3 4"
            3. Run with command "python in.txt out.txt"
            4. Look your optimated result in "out.txt"
    """
    inp = input_from_file()
    expr = solve_greedy(inp, 24)
    output_to_file(expr)

if __name__ == "__main__":
    main()
