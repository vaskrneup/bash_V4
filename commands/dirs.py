"""
True or string is returned if command is found 'Depends on situation' !
"""

from os import path, mkdir, rmdir
from shutil import rmtree


class Dirs:
    def __init__(self, command=None, split_command_minus=None, split_command_space=None, cwd=None, base_dir=None):
        self.command = command  # Gets command !
        self.split_command_minus = split_command_minus  # Gets splitted command using - !
        self.split_command_space = split_command_space

        self.base_dir = base_dir
        self.current_working_dir = cwd.replace('/', '\\')  # Gets current working directory !

    # Sets path for running all the commands !
    def execute(self):
        try:
            if self.split_command_minus[0] == "cwd":
                return self.cwd()
            elif self.split_command_space[0] == "cd":
                return self.cd
            elif self.command[:5] == "mkdir":
                return self.create_dir()
            elif self.command[:5] == "rmdir":
                return self.remove_dir()
            else:
                return False
        except IndexError:
            pass

    # removes directory !
    def remove_dir(self):
        dir_name = self.command[5:].strip()  # gains directory name !
        dir_path = f"{self.current_working_dir}\\{dir_name}"  # gains dir path !

        if path.isdir(dir_path):  # Checks if the dir exist or not !
            try:
                rmdir(dir_path)  # Removes if dir is empty !
            except OSError:
                rm = input("remove NON Empty dir [y|n] : ")
                if rm == "y":
                    rmtree(dir_path)  # Removes if dir is not empty !
        else:
            print("Directory Doesnt Exist !")
        return True

    # Creates empty directory !
    def create_dir(self):
        dir_name = self.command[5:].strip()  # gains directory name !
        dir_path = f"{self.current_working_dir}\\{dir_name}"  # gains dir path !

        if path.isdir(dir_path):  # checks if dir already exists !
            print("Directory already exist !")
        else:
            mkdir(dir_path)  # makes dir !

        return True

    # prints current working dir !
    def cwd(self):
        print(self.current_working_dir)
        return True

    # Changes directory 'RETURNS STRING OF PATH OF NEW WORKING DIR'
    # OR RETURNS TRUE if Dir doesnt exist !
    @property
    def cd(self):
        # Gets current path !
        current_folder_path = path.join(self.current_working_dir, f"{self.command[2:].strip()}")
        # gives name of dir !
        temp_data = [i for i in self.split_command_space[1].strip()]
        # checks if folder exists !
        folder_exist = True

        try:
            # Checks if there is misleading argument !
            if self.split_command_space[1].strip() == ".":
                return True
            # takes back to one dir !
            if self.split_command_space[1].strip() == "..":
                # splits dir of current path !
                temp = self.current_working_dir.split("\\")
                # removes last folder from the list of current path !
                temp.pop()
                # joins the directory again using \\ !
                self.current_working_dir = "\\".join(temp)

                if self.current_working_dir[-1] == ":":
                    return self.current_working_dir + "\\"
                return self.current_working_dir

            # TODO : Code Not required !
            # Checks for misleading data !
            for i in range(len(temp_data)-1):
                if temp_data[i] == temp_data[i + 1] == ".":
                    folder_exist = False
            if not folder_exist:
                print('No such folder !')
                return True

            # Joins new path and returns it !
            elif path.isdir(current_folder_path):   # checks if dir exists !
                # join the new dir with current path !
                current_folder_path.replace("/", "\\")
                self.current_working_dir = path.join(current_folder_path)
                if self.current_working_dir[-1] == ":":
                    return self.current_working_dir + "\\"
                return self.current_working_dir.replace("/", "\\")
            else:
                print("No such folder !")
                return self.current_working_dir
        # catch if no folder is provided !
        except IndexError:
            print("Please specify the folder !")
            return self.current_working_dir


if __name__ == "__main__":
    Dirs()
