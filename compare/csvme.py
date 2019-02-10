from main_compare import main_bf, main_gr
import csv


def export_to_csv(algo="bf"):
    result = main_bf() if algo == "bf" else main_gr()
    fout_name = make_file_name(algo)
    outfile = open(fout_name, 'w', newline='')
    writer = csv.writer(outfile)
    writer.writerows(result)


def import_from_csv(algo="bf"):
    fin_name = make_file_name(algo)
    with open(fin_name, 'r') as f:
        reader = csv.reader(f)
        zip_result = list(reader)
    return zip_result


def make_file_name(algo):
    fout_name = list('./output_.csv')
    fout_name.insert(9, algo)
    fout_name = ''.join(fout_name)
    return fout_name
