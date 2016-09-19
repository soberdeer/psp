import re


def start():
    global file_name
    file_name = input("Please, input file name (ex: text.txt)\n")
    start() if not file_name else mode_select()
    mode_select()


def mode_select():
    mode = input("Please, select mode (r/w):\n")
    read_mode() if mode == 'r' else write_mode()


def read_mode():
    read_file = open(file_name, 'r')
    print(read_file.read())
    read_file.close()


def write_mode():
    global file
    numbers = []
    file = open(file_name, 'a')
    amount = is_int(input("Please, enter amount of numbers\n"))
    print("Please, enter numbers (one per line)\n")
    for i in range(amount):
        enter = input()
        is_empty(enter)
        num = is_real(enter)
        numbers.append(num)
    save(numbers)


def is_empty(enter):
    if enter == "":
        print("Empty string\n")
        write_mode()
    else:
        return


def is_int(num):
    if num.isdigit() and int(num) >= 0:
        return int(num)
    else:
        raise ValueError("Amount must be an integer")


def is_real(num):
    if num.isdigit():
        return int(num)
    elif re.match("\d+\.\d+", num):
        return float(num)
    else:
        raise ValueError("Amount or number is not a real numbers")


def save(numbers):
    decision = input("Save and close? y/n \n")
    if decision == 'Y' or decision == 'y':
        lines = ("\n" + "\n".join(map(str, numbers)))
        file.write(lines)
        file.close()
        print("File saved and closed")
    elif decision == 'N' or decision == 'n':
        mode_select()
    else:
        print('You should print only "y" or "n"')


start()