from A6 import inputs as inputs
import os


def main():
    global path
    file_path = input("Please enter the file path:\n")
    if os.access(os.path.dirname(file_path), os.W_OK):
        path = file_path
        mode_select()
    else:
        print("You might have done a mistake.")
        exit_choice()


# from here can get to read, write or modify mode
def mode_select():
    global file
    mode = input("Please, select mode, read, write or modify (r/w/m):\n").lower()
    if inputs.command_valid_input(['r', 'w', 'm'], mode):
        if mode == 'r':
            read_mode()
        elif mode == 'w':
            file = open(path, 'w')
            write_mode()
        else:
            file = open(path, 'r+')
            modify_mode()
    else:
        mode_select()


# read and print numbers
def read_mode():
    read_file = open(path, 'r')
    print(read_file.read())
    read_file.close()


# write numbers to the file
def write_mode():
    numbers = []
    amount = int(inputs.is_int("Please, enter amount of numbers/arrays.\n"))
    for i in range(0, amount):
        enter = inputs.enter_number()
        numbers.append(enter)
    with file as f:
        f.writelines("\n".join(numbers))
    file.close()


# provide functions: continue, replace, delete, insert and accept remaining
def modify_mode():
    lines = []
    for line in file:
        lines.append(' '.join(line.split()))
    file.close()
    accept_remain = False
    for i, line in enumerate(lines):
        if not accept_remain:
            print("Please, select what to do with numbers.\n")
            print("Position {}, Number: {}".format((i + 1), line))
            action = input("Choose one of the actions: Continue (c), Replace (r), Delete (d), Insert (i)\n")
            if inputs.command_valid_input(['c', 'r', 'd', 'i'], action):
                if action == 'c':
                    continue
                elif action == 'r':
                    lines[i] = inputs.enter_number()
                    print("Position %s successfully replaced" % str(i + 1))
                elif action == 'd':
                    lines.pop(i)
                    print("Position %s successfully deleted\n" % str(i + 1))
                else:
                    insert(i, lines)
            else:
                modify_mode()

            remain = input("Accept the remaining numbers? y/n\n")
            if remain == 'y':
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
    decision = input("You are currently at the position %s\nInsert the number? y/n\n" % str(i + 1)).lower()
    if inputs.command_valid_input(['y', 'n'], decision):
        if inputs.yes_no(decision):
            position = insert_where(left)
            valid_number = inputs.enter_number()
            lines.insert(int(position), valid_number)
            print("Number %s successfully inserted\n" % valid_number)
        else:
            modify_mode()
    else:
        print("Wrong command")
        insert(i, lines)


# returns the position to insert.
# if 'a' -> after current OR returns num of the position in the tail.
def insert_where(left):
    where = ""
    valid = False
    while not valid:
        position = inputs.is_int(
            str(left) + " numbers left. Where insert the number/array? Integer num or After current (a)\n")
        if position == 'a' or (position.isdigit() and 0 < int(position) <= left):
            if position == 'a':
                where = "1"
                valid = True
            else:
                where = str(int(position) - 1)
                valid = True
        else:
            print('Command should be "a" or an integer, please, try again')
            valid = False
    return where


# ask user if he wants to try again or exit
def exit_choice():
    input_ = input("Would you like to try again? y/n\n").lower()
    if inputs.command_valid_input(['y', 'n'], input_):
        if inputs.yes_no(input_):
            main()
        else:
            print('exit')
            quit()
    else:
        exit_choice()


# save as which file
def save_changes(lines):
    save_path = ""
    decision = input("Do you want to save file? 1 = save, 2 = save new file, n = exit without save\n").lower()
    if inputs.command_valid_input(['1', '2'], decision):
        if decision == "1":
            save_path = path
        elif decision == "2":
            save_path = inputs.is_valid_new_file()
        else:
            quit()
    else:
        print("Wrong command.\n")
        save_changes(lines)
    save_file(save_path, lines)


# saves file in save_path
def save_file(save_path, lines):
    file_ = open(save_path, 'w')
    file_.truncate()
    with file_ as f:
        f.writelines("\n".join(lines))
        file_.close()


main()