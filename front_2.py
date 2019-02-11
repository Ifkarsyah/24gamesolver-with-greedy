import sys


# print('Argument List:', str(sys.argv))


def input_from_file():
    with open(sys.argv[1], "r") as fin:
        raw_input = list(map(int, fin.read().split()))
    return raw_input


def output_to_file(expr):
    with open(sys.argv[2], "w") as fout:
        fout.write(expr)
