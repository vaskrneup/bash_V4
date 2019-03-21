from os import listdir, path, remove
from styleMain.color import *


class File:
    def __init__(self, command=None, split_command_minus=None, split_command_space=None, cwd=None, base_dir=None):
        self.command = command  # gets command !
        self.split_command_minus = split_command_minus  # gets command splited with '-' !
        self.split_command_space = split_command_space  # gets command splited with '<SPACE>' !

        self.base_dir = base_dir  # gets the dir where bash.py is located !
        self.current_working_dir = cwd  # Gets current working directory !

    # Sets path for running all the commands !
    def execute(self):
        try:
            if self.split_command_minus[0].strip() == "ls":
                return self.ls()
            elif self.command[:3] == "cat":
                return self.cat()
            elif self.command[:5] == "touch":
                return self.touch()
            elif self.command[:2] == "rm":
                return self.remove_file()
            else:
                return False
        except IndexError:
            pass

    # deletes file !
    def remove_file(self):
        file_name = self.command[2:].strip()  # gets file name !
        file_path = f"{self.current_working_dir}/{file_name}"  # gets file path !

        if path.isfile(file_path):  # checks if file exist !
            remove(file_path)  # removes the file !
            # print(colored("deleted !", 'red', attrs=['bold']))
            print(red("deleted !"))
        else:
            # print(colored("File doesnt exist !", 'yellow', attrs=['bold']))
            print(yellow("File doesnt exist !", attrs=['bold']))

        return True

    # creates new file !
    def touch(self):
        file_name = self.command[5:].strip()  # gets name of file to be created !
        # gets path where file is to be created !
        file_path = f"{self.current_working_dir}/{file_name}"

        if path.isfile(file_path):  # checks if file exist !
            # Confirm rewrite existing file !
            del_or_not = input("Overwrite[O] dont write[D] : ")
            if del_or_not.lower() == "o":
                print("overwritten !")
                working_file = open(file_path, 'w')  # rewrite existing file !
                working_file.close()  # close the file !
            else:
                print("not deleted !")
        else:
            print("Created !")
            working_file = open(file_path, 'w')  # Creates new file !
            working_file.close()  # closes file !

        return True

    # outputs the objects of file !
    def cat(self):
        # outputs the objects of file with color !
        def print_file_data(file_path):
            my_file = open(file_path, 'r')  # open file for read !
            print(green("=================================================================="*2))
            for line in my_file:  # grabs lines of file !
                line = line[:-1]  # removes extra \n from line !
                print(cyan(line))
            my_file.close()  # closes the file !s
            print("\n")
            print(green("=================================================================="*2))
            return True

        file_to_read = self.command.split(' ')[1].strip()  # grabs the file to read !

        # checks if file exist or not in same dir !
        if path.isfile(f"{self.current_working_dir}/{file_to_read}"):
            # runs print_file_data function and returns True
            return print_file_data(f"{self.current_working_dir}/{file_to_read}")
        # checks if file exist or not in whole computer !
        elif path.isfile(f"{file_to_read}"):
            # runs print_file_data function and returns True
            return print_file_data(f"{file_to_read}")
        else:
            print("File Not Found !")
            return True

    # outputs list of files and folders in path !
    def ls(self):
        file_list_in_cwd = listdir(self.current_working_dir)  # returns list of files in current working directory !

        for file in file_list_in_cwd:  # loops through files in CWD !
            # checks if data is file !
            if path.isfile(f"{self.current_working_dir}\\{file}"):
                print(cyan(f"*{file}"))  # Prints file Name !
            # checks if data is folder|dir !
            elif path.isdir(f"{self.current_working_dir}\\{file}"):
                print(magenta(f"@{file}"))  # Prints directory Name !
            # if any complication occurs this will handle it !
            else:
                print(file)  # Prints remaining !

        if "c" in self.split_command_minus:  # Checks if c or count is given as argument !
            print(blue(f"\nCount :", attrs=['bold']),
                  yellow(f" {len(file_list_in_cwd)}",
                         attrs=['bold']))  # Prints number of files in directory !
        return True


if __name__ == "__main__":
    File()
