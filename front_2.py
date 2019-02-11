import sys


# print('Argument List:', str(sys.argv))


def input_from_file():
    with open(sys.argv[1], "r") as fin:
        raw_input = list(map(int, fin.read().split()))
    return raw_input


def output_to_file(expr):
    with open(sys.argv[2], "w") as fout:
        fout.write(expr)

# CARA FRONT END 1 BUAT DIGABUNGIN
# 1. AMBIL DATA raw_input DARI input_from_file()
# 2. TampilinDiGUI(raw_input), format raw_input = [1,2,3,4]
# 3. AMBIL DATA expr DARI output_from_file()
# 4. TampilindiGUI(expr), format expr="1+2+3+4"
