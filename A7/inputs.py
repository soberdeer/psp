import re
import os
MAX_ARRAY = 10


# checks if inputted command is from the list
def command_valid_input(commands, input_):
    if input_ in commands:
        return True
    else:
        print('You should print valid command.')
        return False


def yes_no(input_):
    if input_ == 'y':
        return True
    elif input_ == 'n':
        return False


# if num is_empty
def is_empty(num):
    not_empty = False
    while not not_empty:
        if num != "":
            not_empty = True
        else:
            print("Empty string\n")
            not_empty = False
    return not_empty


# enter real number or array
def enter_number():
    valid = False
    number = ""
    while not valid:
        num = input("Please, enter a number or an array (split with whitespace), max length = 10\n")
        if not re.search(' ', num):
            if num.isdigit():
                number = num
                valid = True
            elif re.match("\d+\.\d+", num):
                number = num
                valid = True
            else:
                if not input_corrector():
                    valid = True
        else:
            if enter_array(num):
                valid = True
                number = num
            else:
                if not input_corrector():
                    valid = True
    return number


# check if string array has real numbers only and length less than 10
def enter_array(string):
    valid = False
    array = string.split()
    if len(array) < MAX_ARRAY:
        for i in array:
            if i.isdigit():
                valid = True
            elif re.match("\d+\.\d+", i):
                valid = True
            else:
                print("Entered value is not a number.")
                valid = False
    else:
        print("Array is too long.")
        valid = False
    return valid


# check if input is int
def is_int(string):
    valid = False
    num = ""
    while not valid:
        number = input(string)
        if number.isdigit():
            num = number
            valid = True
        else:
            print("Wrong quantity.")
            if not input_corrector():
                num = number
                valid = True
    return num


# checks if new file path is correct and there is no existing file
def is_valid_new_file():
    valid = False
    value = ''
    pattern = re.compile('^(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$))')
    while not valid:
        value = input("Enter new path and filename.\n")
        if pattern.match(value) and not os.path.isfile(value):
            valid = True
        else:
            print("Invalid filename or path\n")
            if not input_corrector():
                valid = True
    return value


# gives user another chance
def input_corrector():
    valid = False
    while not valid:
        input_ = input("Try again? y/n\n").lower()
        if input_ == "y":
            valid = True
        elif input_ == "n":
            quit()
        else:
            print("Wrong command")
            valid = False
    return valid


def linear_regression_file_is_valid(file_):
    result = True
    f = load_file_to_array(file_)
    if len(f) == 0:
        result = False
    for i in range(0, len(f)):
        if len(f[i]) == 3:
            for j in range(0, 3):
                if is_valid_number(f[i][j]):
                    pass
                else:
                    result = False
                    break
        else:
            result = False
            break
    return result


def load_file_to_array(file_):
    f = [[int(float(j)) for j in i] for i in [item.split(',') for item in [' '.join(line.split()) for line in file_]]]
    return f


def is_valid_number(num):
    return True if re.match("\d+\.\d+", num) or num.isdigit() else False