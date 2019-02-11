import sys


# print('Argument List:', str(sys.argv))


def input_from_file():
    with open(sys.argv[1], "r") as fin:
        inp = sorted(map(int, fin.read().split()), reverse=True)
    return inp


def output_to_file(expr):
    with open(sys.argv[2], "w") as fout:
        fout.write(expr)
