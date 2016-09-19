import os
# C:\psp\A3\2B.py


def main():
    global path
    file_path = input("Please enter the file path:\n")
    if check_filename(file_path):
        path = file_path
        read_file()
    else:
        print("You might have done a mistake.")
        main()


def check_filename(name):
    if os.access(os.path.dirname(name), os.W_OK):
        return True
    else:
        return False


def read_file():
    file = open(path, 'r')
    lines = file.readlines()
    file.close()
    print(loc_counter(lines))


def loc_counter(lines):
    valid_lines = 0
    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("#") or line.startswith('"'):
            continue
        else:
            valid_lines += 1
    return valid_lines


main()