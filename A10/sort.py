def merge_sort(file):
    lines_f = []
    lines = []
    for line in file:
        lines_f.append(' '.join(line.split()))
    for item in lines_f:
        lines.append(item.split())
    final_lst = convert(lines)
    file.close()
    print_table(final_lst)
    col = input('Please, choose the column by which you want to sort: 1 for Loc, 2 for Loc/Method\n')
    sort_table(final_lst, int(col)) if col == '1' or col == '2' else print('capital escape!')


def convert(lines):
    return [[float(i) for i in j] for j in lines]


def sort_table(table, col):
    table.sort(key=lambda x: x[col])
    print_table(table)


def print_table(lst):
    for elem in lst:
        print(elem)
