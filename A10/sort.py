import operator


def merge_sort(file):
    lines = []
    cols = [0, 1]
    lines_f = [[]]
    for rec in file:
        for l, col in lines_f:
            l.append(float(lines_f))
    print(lines_f)
    file.close()


file = open('/Users/telse/IdeaProjects/psp/1b.txt', 'r+')
merge_sort(file)