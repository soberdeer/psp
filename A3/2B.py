import re
import os


def main():
    global path
    file_path = input("Please enter the file path:\n")
    if check_filename(file_path):
        path = file_path
        mode_select()
    else:
        print("You might have done a mistake.")
        main()


# from here can get to read, write or modify mode
def mode_select():
    global file
    mode = input("Please, select mode, read, write or modify (r/w/m):\n").lower()
    if command_valid_input(['r', 'w', 'm'], mode):
        if mode == 'r':
            read_mode()
        elif mode == 'w':
            file = open(path, 'a')
            write_mode()
        else:
            file = open(path, 'r+')
            modify_mode()
    else:
        mode_select()


def read_mode():
    read_file = open(path, 'r')
    print(read_file.read())
    read_file.close()


def write_mode():
    numbers = []
    amount = is_int(input("Please, enter amount of numbers\n"))
    print("Please, enter numbers (one per line)\n")
    for i in range(amount):
        enter = input()
        numbers.append(is_valid(enter))
    save(numbers)


# provide functions: continue, replace, delete, insert and accept remaining
def modify_mode():
    lines = file.readlines()
    accept_remain = False
    for i, line in enumerate(lines):
        if not accept_remain:
            print("Please, select what to do with numbers.\n")
            print("Index {}, Number: {}".format((i + 1), line))
            action = input("Choose one of the actions: Continue (c), Replace (r), Delete (d), Insert (i)\n")
            if command_valid_input(['c', 'r', 'd', 'i'], action):
                if action == 'c':
                    continue
                elif action == 'r':
                    lines[i] = replace()
                    print("Index " + str(i + 1) + " successfully replaced")
                elif action == 'd':
                    lines.pop(i)
                    print("Index " + str(i + 1) + " successfully deleted\n")
                else:
                    insert(i, lines)
            else:
                modify_mode()

            remain = input("Accept the remaining numbers? y/n\n")
            if command_valid_input(['y', 'n'], remain):
                if yes_no(remain):
                    accept_remain = True
                    continue

        else:
            pass
    else:
        pass
    save_changes(lines)


# insert the number after current position OR before the position.
def insert(i, lines):
    left = len(lines) - (i + 1)
    decision = input("You are currently at the position " + str(i + 1) + "\nInsert the number? y/n\n").lower()
    if command_valid_input(['y', 'n'], decision):
        if yes_no(decision):
            position = insert_where(left)
            valid_number = is_valid(input("Print the value to insert\n"))
            lines.insert(int(position), valid_number)
            print("Number " + str(valid_number) + " successfully inserted\n")
        else:
            modify_mode()
    else:modify_mode()


# returns the position to insert.
# if 'a' -> after current OR returns num of the position in the tail.
def insert_where(left):
    where = 0
    position = input(
        str(left) + " numbers are left. Where insert the number? Integer num or After current (a)\n").lower()
    is_empty(position)
    if position == 'a' or (position.isdigit() and 0 < int(position) <= left):
        if position == 'a':
            where = 1
        else:
            where = position
    else:
        print('Command should be "a" or an integer, please, try again')
        insert_where(left)
    return where


# replaces current number
def replace():
    string_num = input("Please, enter replacement number\n").lower()
    is_empty(string_num)
    num = is_real(string_num)
    return num


# checks if number is valid e.g. not empty and real
def is_valid(num):
    is_empty(num)
    return is_real(num)


def is_empty(num):
    if num == "":
        print("Empty string\n")
        write_mode()
    else:
        return


# checks if number of values >= 0 and int
def is_int(num):
    if num.isdigit() and int(num) >= 0:
        return int(num)
    else:
        print("Amount must be an integer")
        write_mode()


# checks numbers to be inserted into file
def is_real(num):
    if num.isdigit():
        return int(num)
    elif re.match("\d+\.\d+", num):
        return float(num)
    else:
        return


def check_filename(name):
    if os.access(os.path.dirname(name), os.W_OK):
        return True
    else:
        return False


def is_file_exist(name):
    if os.path.isfile(name):
        return True
    else:
        return False


# save as which file
def save_changes(lines):
    decision = input("Do you want to save changes into new file? y/n\n").lower()
    if command_valid_input(['y', 'n'], decision):
        if yes_no(decision):
            create_new_file(lines)
        else:
            save(lines)
    else:
        save_changes(lines)


def create_new_file(lines):
    file_path = input("Enter the path and the name for the new file\n")
    if file_path == "" or is_file_exist(file_path):
        print("You might have done a mistake, there is an empty space or existing file.")
        create_new_file(lines)
    elif check_filename(file_path):
        new_file = open(file_path, "w")
        with new_file as f:
            f.writelines(map(str, lines))
            new_file.close()
        print("New file saved and closed")
    else:
        print("Wrong file name or path")
        create_new_file(lines)


def save(lines):
    decision = input("Save and close? y/n \n")
    if command_valid_input(['y', 'n'], decision):
        if yes_no(decision):
            file.writelines(("\n" + "\n".join(map(str, lines))))
            file.close()
            print("File saved and closed")
        else:
            mode_select()


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


main()