from pickle import dump, load
from os.path import isfile

from bash import Bash


class Function:
    def __init__(self, command=None, split_command_minus=None, split_command_space=None, cwd=None, base_dir=None):
        self.command = command  # gets base dir !
        self.split_command = split_command_minus  # gets command list splited with '-' !
        self.split_command_space = split_command_space  # gets command list splited with '<SPACE>'' !
        self.base_dir = base_dir  # gets path of bash.py !

        self.current_working_dir = cwd  # Gets current working directory !

    # Sets path for running all the commands !
    def execute(self):
        if self.command[:4] == "func":
            return self.func_maker()
        elif self.command[-2:] == "()":
            return self.func_runner()
        else:
            return False

    # creates a function !
    def func_maker(self):
        # takes function input and saves it !
        def create_function():
            print("New function created !")

            # loops until function is complete !
            while True:
                command_entry = input(">>> ")
                if command_entry == "":
                    command_entry = input(">>> ")
                    if command_entry == "":
                        break
                    else:
                        # adds new command to end of list !
                        commands.append(command_entry)
                else:
                    # adds new command to end of list !
                    commands.append(command_entry)
            dump(commands, open(file_path, 'wb'))  # writes the data in binary !

        commands = []  # init commands to save !
        file_name = self.command[4:].strip()  # gets command name !
        # makes path for command to be saved !
        file_path = f"{self.base_dir}/CDF/{file_name}.dll"

        # checks if command already exist !
        if isfile(file_path):
            # checks if user wants to overwrite the command !
            yes_or_no = input("Rewrite the function [y/n]: ")
            if yes_or_no.lower() == "y":
                create_function()  # creates the function !
            else:
                print("Function Not over written!")
        else:
            create_function()  # creates the function !

        return True

    # runs the existing function !
    def func_runner(self):
        file_name = self.command[:-2].strip()  # grabs command name !
        file_path = f"{self.base_dir}\\CDF\\{file_name}.dll"  # makes path for command !

        if isfile(file_path):  # checks if command exist !
            my_file = open(file_path, 'rb')  # opens command !
            command_list = load(my_file)  # loads command data in list !
            my_file.close()  # close command !
            Bash(command=command_list)  # returns the command to the main program !
        else:
            print("Command doesn't exist !")

        return True
