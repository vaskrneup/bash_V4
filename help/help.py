from os import system
from styleMain.color import *


class HelpFinder:
    def __init__(self, command=None, command_split_minus=None, command_split_space=None, base_file_location=None):
        self.base_file = base_file_location
        self.command = command
        self.command_split_minus = command_split_minus
        self.command_split_space = command_split_space

    def execute(self):
        if self.command == "help":
            return self.help_all()
        else:
            return False

    def help_all(self):
        help_file = open(f"{self.base_file}\\help\\AllHelpText.txt", 'r')
        file_text = help_file.read()
        help_file.close()
        print(magenta("\n"+file_text))
        print('\n=============================SYSTEM HELP====================================\n')
        system("help")
        return True


if __name__ == "__main__":
    HelpFinder()
