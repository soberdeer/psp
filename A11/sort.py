from A11 import regression as r


def is_sort(file):
    lst = convert(file_to_list_of_lists(file))
    file.close()
    lines = []
    decision = input('Print 0 for stats else 1 for sort\n')
    if decision == '0':
        lines = stats(lst)
    elif decision == '1':
        lines = sort(lst)
    else:
        print("CAPITULATION")
    return lines


def stats(lst):
    input_ = input("Please, choose the column to calculate: 1 for LOC, 2 for LOC/Method")
    valid = False
    lines = []
    while not valid:
        if input_ == '1' or input_ == '2':
            string = ("LOC" if input_ == '1'else "LOC/Method")
            lines.append("Max %s: %0.2f" % (string, max_col(lst, int(input_))))
            lines.append("Min %s: %0.2f" % (string, min_col(lst, int(input_))))
            lines.append("Std_dev %s: %0.2f" % (string, std(lst, int(input_))))
            print("\n".join(lines))
            valid = True
        else:
            print("Wrong input")
            valid = False

    return lines


def std(lst, col):
    b1 = r.calculate_b1(lst, col)
    if col == 1:
        b0 = avg_col(lst, 2) - b1 * avg_col(lst, 1)
    else:
        b0 = avg_col(lst, 1) - b1 * avg_col(lst, 2)
    return r.std_deviation(lst, b0, b1)


def avg_col(lst, col):
    return sum([l[col] for l in lst]) / len(lst)


def min_col(lst, col):
    return min(l[col] for l in lst)


def max_col(lst, col):
    return max(l[col] for l in lst)


def file_to_list_of_lists(file):
    lines_f = []
    lines = []
    for line in file:
        lines_f.append(' '.join(line.split()))
    for item in lines_f:
        lines.append(item.split())
    return lines


def convert(lines):
    return [[float(i) for i in j] for j in lines]


def sort(lst):
    col = input('Please, choose the column by which you want to sort: 1 for Loc, 2 for Loc/Method\n')
    sorted_ = []
    valid = False
    while not valid:
        if col == '1' or col == '2':
            sorted_ = sort_table(lst, int(col))
            valid = True
        else:
            print('capital escape!')
            valid = False
    return sorted_


def sort_table(table, col):
    table.sort(key=lambda x: x[col])
    table = [', '.join(x) for x in [[str(j) for j in i] for i in table]]
    print_table(table)
    return table


def print_table(lst):
    for elem in lst:
        print(elem)