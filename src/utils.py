import os
import platform


def clear_screen():
    clear_command = "cls" if platform.system() == "Windows" else "clear"
    os.system(clear_command)


def print_header(title):
    border = "=" * (8 + len(title)) + "\n"
    print("{0}||  {1}  ||\n{0}".format(border, title))
